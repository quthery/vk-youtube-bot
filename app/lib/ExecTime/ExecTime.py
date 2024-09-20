import time

async def exec_time(function) -> dict:
	start = time.time()

	result = await function()

	end = time.time()
	exec_time = end - start
	print(f"Execution time: {end - start} seconds")
	return {"video": result, "exec_time": exec_time}