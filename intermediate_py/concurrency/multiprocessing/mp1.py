import multiprocessing
import time

def heavy_calculation(n):
    print(f"🔢 Calculating {n}...")
    result = sum(i * i for i in range(n))
    print(f"✅ Done {n}: {result}")
    return result

if __name__ == "__main__":     
    numbers = [1000000, 2000000, 3000000]

    # Without multiprocessing
    start = time.time()
    for n in numbers:
        heavy_calculation(n)
    print(f"Without MP: {time.time()-start:.2f}s")

    # With multiprocessing
    start = time.time()
    processes = []

    for n in numbers:
        p = multiprocessing.Process(
            target=heavy_calculation,
            args=(n,)
        )
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"With MP: {time.time()-start:.2f}s")