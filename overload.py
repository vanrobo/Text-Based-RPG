import threading
import sys
import time

def perform_task_with_loading(task_name="Generic Task", duration=5):
    """
    Performs a task and shows a loading animation internally.
    The loader starts when this function is called and stops when the task work is done.
    """
    # 1. Event to signal the loader when this specific task's work is done
    #    This event is local to this function call.
    generate_event = threading.Event()

    # 2. Define the loader animation function (can be a nested function)
    def _internal_loader_animation():
        animation_chars =  ['/','-','\\','|']




        idx = 0
        print("")
        sys.stdout.flush()

        while not generate_event.is_set():
            sys.stdout.write(f"\r{animation_chars[idx % len(animation_chars)]}   ")
            sys.stdout.flush()
            idx += 1
            time.sleep(0.2)
        
        clear_line_animation = " " * 10  # Adjust number of spaces if your animation is longer
        sys.stdout.write(f"\r{clear_line_animation}\r") # Overwrite with spaces, then CR
        sys.stdout.flush()

    # 3. Create and start the loader thread
    loader_thread = threading.Thread(target=_internal_loader_animation)
    loader_thread.daemon = True  # Good for helper threads
    loader_thread.start()

    try:
        for i in range(duration):
            # Simulate some part of the main work
            time.sleep(1)
            # You could print progress from the main task if needed,
            # but it might interfere with the \r of the loader.
            # print(f"  (Debug: '{task_name}' work step {i+1}/{duration})")
    finally:
        if loader_thread and loader_thread.is_alive():
        # 4. Signal the loader thread that the main work is complete
            generate_event.set()
            loader_thread.join(timeout=1)
            print("") # Give it a moment to clean up
        # 5. Wait for the loader thread to finish its final print and exit
        #    This ensures the "Loading complete!" message is printed before
        #    the main function returns or prints further.

    # The loader thread has now stopped.
    # The perform_task_with_loading function can now return.

perform_task_with_loading()