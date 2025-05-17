import os
import stat


def check_file_permissions(file_path: str) -> dict:
    """
    Check file permissions and return a dictionary with details
    """
    try:
        # Check if file exists
        exists = os.path.exists(file_path)
        
        # Get file stats
        stats = os.stat(file_path) if exists else None
        
        # Check permissions
        can_read = os.access(file_path, os.R_OK) if exists else False
        can_write = os.access(file_path, os.W_OK) if exists else False
        
        # Get permission bits
        mode = oct(stats.st_mode)[-3:] if exists else '---'
        
        return {
            'exists': exists,
            'mode': mode,
            'readable': can_read,
            'writable': can_write,
            'owner': stats.st_uid if exists else None,
            'group': stats.st_gid if exists else None,
            'size': stats.st_size if exists else 0
        }
    except Exception as e:
        return {
            'exists': exists,
            'error': str(e)
        }

def test_file_writable(file_path: str) -> bool:
    """
    Test if file is writable by attempting to write to it
    """
    try:
        # Try to write to the file
        with open(file_path, 'w') as f:
            f.write("Test direct write\n")
        
        # Verify the write
        with open(file_path, 'r') as f:
            content = f.read()
            return 'Test direct write' in content
    except Exception as e:
        print(f"Error testing file write: {e}")
        return False
