import sys
import os
import mailbox

def split_mbox(filename, chunk_size):
    if not os.path.exists(filename):
        print(f"File {filename} not found")
        return
        
    mbox = mailbox.mbox(filename)
    basename = os.path.splitext(filename)[0]
    
    chunk_size_bytes = chunk_size * 1024 * 1024  # Convert MB to bytes
    current_size = 0
    current_chunk = 1
    message_count = 0
    
    output_path = f"{basename}_{current_chunk}.mbox"
    output_mbox = mailbox.mbox(output_path)
    
    for message in mbox:
        message_size = len(str(message).encode('utf-8'))
        if current_size + message_size > chunk_size_bytes and message_count > 0:
            print(f"Created file '{output_path}', size={current_size/1024/1024:.0f}Mb, messages={message_count}")
            output_mbox.close()
            current_chunk += 1
            message_count = 0
            current_size = 0
            output_path = f"{basename}_{current_chunk}.mbox"
            output_mbox = mailbox.mbox(output_path)
        
        output_mbox.add(message)
        current_size += message_size
        message_count += 1
    
    output_mbox.close()
    print(f"Created file '{output_path}', size={current_size/1024/1024:.0f}Mb, messages={message_count}")
    print("Done")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python mbox-splitter.py filename.mbox size")
        sys.exit(1)
        
    filename = sys.argv[1]
    try:
        chunk_size = int(sys.argv[2])
    except ValueError:
        print("Size must be a positive integer")
        sys.exit(1)
        
    split_mbox(filename, chunk_size)
