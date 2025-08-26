#!/usr/bin/env python3
"""
Test script to verify batch processing functionality.

This script sends concurrent requests to test the batch processing capabilities.
"""

import asyncio
import aiohttp
import json
import time
from typing import List

async def send_request(session: aiohttp.ClientSession, url: str, request_data: dict, request_id: int):
    """Send a single request and measure timing."""
    start_time = time.time()
    try:
        async with session.post(url, json=request_data) as response:
            if response.status == 200:
                result = await response.json()
                end_time = time.time()
                return {
                    'request_id': request_id,
                    'success': True,
                    'latency': end_time - start_time,
                    'response': result['choices'][0]['message']['content'][:100] + '...' if len(result['choices'][0]['message']['content']) > 100 else result['choices'][0]['message']['content']
                }
            else:
                error_text = await response.text()
                return {
                    'request_id': request_id,
                    'success': False,
                    'error': f"HTTP {response.status}: {error_text}",
                    'latency': time.time() - start_time
                }
    except Exception as e:
        return {
            'request_id': request_id,
            'success': False,
            'error': str(e),
            'latency': time.time() - start_time
        }

async def test_batch_performance(server_url: str = "http://localhost:8000", num_requests: int = 16):
    """Test batch processing performance by sending concurrent requests."""
    
    print(f"🧪 Testing batch processing with {num_requests} concurrent requests")
    print(f"Server: {server_url}")
    print("=" * 80)
    
    # Prepare test requests
    test_questions = [
        "What is 2 + 2?",
        "Solve: 15 * 3 + 7 = ?",
        "If a train travels 60 mph for 2.5 hours, how far does it go?",
        "Calculate the area of a circle with radius 5.",
        "What is the square root of 144?",
        "If I have 20 apples and give away 8, how many do I have left?",
        "Convert 32°F to Celsius.",
        "What is 25% of 80?",
        "Solve for x: 2x + 5 = 15",
        "How many seconds are in 3 minutes?",
        "What is 7 factorial (7!)?",
        "If a rectangle has length 8 and width 6, what is its perimeter?",
        "What is 3^4 (3 to the power of 4)?",
        "Calculate: (10 + 5) * 2 - 8",
        "What is 1/4 + 1/3?",
        "If gas costs $3.50 per gallon and I need 12 gallons, how much will I pay?"
    ]
    
    # Create requests
    requests = []
    for i in range(num_requests):
        question = test_questions[i % len(test_questions)]
        request_data = {
            "model": "llada-8b-instruct",
            "messages": [{"role": "user", "content": question}],
            "max_tokens": 64,
            "temperature": 0.0,
            "steps": 64,
            "block_length": 32,
            "generation_algorithm": "dual_cache"
        }
        requests.append((request_data, i))
    
    # Test concurrent requests
    start_time = time.time()
    
    connector = aiohttp.TCPConnector(limit=100, limit_per_host=50)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [
            send_request(session, f"{server_url}/v1/chat/completions", req_data, req_id)
            for req_data, req_id in requests
        ]
        
        print("⏳ Sending concurrent requests...")
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    # Analyze results
    successful_requests = [r for r in results if r['success']]
    failed_requests = [r for r in results if not r['success']]
    
    print("\n📊 **RESULTS**")
    print("=" * 80)
    print(f"Total time: {total_time:.3f} seconds")
    print(f"Successful requests: {len(successful_requests)}/{num_requests}")
    print(f"Failed requests: {len(failed_requests)}")
    print(f"Throughput: {len(successful_requests)/total_time:.2f} requests/second")
    
    if successful_requests:
        latencies = [r['latency'] for r in successful_requests]
        avg_latency = sum(latencies) / len(latencies)
        min_latency = min(latencies)
        max_latency = max(latencies)
        
        print(f"\n⏱️  **LATENCY STATS**")
        print(f"Average latency: {avg_latency:.3f} seconds")
        print(f"Min latency: {min_latency:.3f} seconds")
        print(f"Max latency: {max_latency:.3f} seconds")
    
    if failed_requests:
        print(f"\n❌ **FAILED REQUESTS**")
        for req in failed_requests:
            print(f"Request {req['request_id']}: {req['error']}")
    
    print(f"\n✅ **SAMPLE RESPONSES**")
    for i, req in enumerate(successful_requests[:3]):
        print(f"Request {req['request_id']}: {req['response']}")
    
    print("\n🎯 **BATCH EFFICIENCY**")
    if len(successful_requests) > 8:
        print("✅ High concurrency handled successfully - batching likely working!")
    elif len(successful_requests) > 4:
        print("✅ Moderate concurrency handled - some batching occurring")
    else:
        print("⚠️  Low concurrency - check batch configuration")
    
    return results

async def test_batch_stats(server_url: str = "http://localhost:8000"):
    """Test the batch stats endpoint."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{server_url}/batch/stats") as response:
                if response.status == 200:
                    stats = await response.json()
                    print("📊 **BATCH STATS**")
                    print(f"Max batch size: {stats['max_batch_size']}")
                    print(f"Max wait time: {stats['max_wait_time']} seconds")
                    print(f"Pending requests: {stats['pending_requests']}")
                    print(f"Currently processing: {stats['currently_processing']}")
                else:
                    print(f"❌ Failed to get batch stats: {response.status}")
    except Exception as e:
        print(f"❌ Error getting batch stats: {e}")

async def test_generation_algorithms(server_url: str = "http://localhost:8000"):
    """Test the generation algorithms endpoint."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{server_url}/generation/algorithms") as response:
                if response.status == 200:
                    algorithms = await response.json()
                    print("🔧 **GENERATION ALGORITHMS**")
                    for algo in algorithms.get('algorithms', []):
                        status = "✅" if algo.get('available') else "❌"
                        print(f"{status} {algo['name']}: {algo['description']}")
                else:
                    print(f"❌ Failed to get algorithms: {response.status}")
    except Exception as e:
        print(f"❌ Error getting algorithms: {e}")

async def test_mixed_algorithms(server_url: str = "http://localhost:8000"):
    """Test batch processing with mixed generation algorithms."""
    print("🧪 Testing mixed algorithm batching...")
    
    test_requests = [
        {
            "model": "llada-8b-instruct",
            "messages": [{"role": "user", "content": "What is 5 + 3?"}],
            "max_tokens": 50,
            "generation_algorithm": "basic"
        },
        {
            "model": "llada-8b-instruct",
            "messages": [{"role": "user", "content": "What is 7 * 4?"}],
            "max_tokens": 50,
            "generation_algorithm": "prefix_cache"
        },
        {
            "model": "llada-8b-instruct",
            "messages": [{"role": "user", "content": "What is 12 / 3?"}],
            "max_tokens": 50,
            "generation_algorithm": "dual_cache"
        },
        {
            "model": "llada-8b-instruct",
            "messages": [{"role": "user", "content": "What is 9 - 2?"}],
            "max_tokens": 50,
            "generation_algorithm": "dual_cache"
        }
    ]
    
    start_time = time.time()
    
    async with aiohttp.ClientSession() as session:
        tasks = [
            send_request(session, f"{server_url}/v1/chat/completions", req, i)
            for i, req in enumerate(test_requests)
        ]
        results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    total_time = end_time - start_time
    
    successful = [r for r in results if r['success']]
    print(f"Mixed algorithm test: {len(successful)}/{len(test_requests)} successful in {total_time:.3f}s")
    
    return results

async def main():
    """Main test function."""
    server_url = "http://localhost:8000"
    
    print("🚀 **LLADA BATCH SERVER TEST**")
    print("=" * 80)
    
    # Test health check
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{server_url}/health") as response:
                if response.status == 200:
                    health = await response.json()
                    print("✅ Server is healthy")
                    print(f"Model loaded: {health['model_loaded']}")
                    print(f"Device: {health['device']}")
                    print(f"Batch processor active: {health.get('batch_processor_active', 'N/A')}")
                else:
                    print(f"❌ Server health check failed: {response.status}")
                    return
    except Exception as e:
        print(f"❌ Cannot connect to server: {e}")
        print("Make sure the batch server is running:")
        print("python llada_batch_server.py --model-path GSAI-ML/LLaDA-8B-Instruct")
        return
    
    print()
    
    # Test generation algorithms endpoint
    await test_generation_algorithms(server_url)
    print()
    
    # Test batch stats
    await test_batch_stats(server_url)
    print()
    
    # Test mixed algorithm processing
    await test_mixed_algorithms(server_url)
    print()
    
    # Test batch performance
    await test_batch_performance(server_url, num_requests=16)

if __name__ == "__main__":
    asyncio.run(main())
