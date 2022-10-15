# Asyncio notes

## Asyncio API summarized

- Starting the `asyncio` event loop: `get_event_loop()`
- Calling `async/await` functions: `run_in_executor()`
- Creating a _task_ to be run on the loop: `create_task()`
- Waiting for multiple tasks to be complete: `gather()`
- Closing the loop after all concurrent tasks have completed: `close()`


## Referencesd

- [`async/await` and Why it is awesome](https://youtu.be/m28fiN9y_r8)
