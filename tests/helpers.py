import os, sys, tempfile, struct, numpy as np
import cv2
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 注册所有临时文件路径，供 conftest 自动清理
_created_temp_files: set[str] = set()


def _register(path: str) -> str:
    _created_temp_files.add(path)
    return path


def cleanup_temp_files():
    for p in list(_created_temp_files):
        try:
            os.remove(p)
        except OSError:
            pass
        _created_temp_files.discard(p)


def make_test_image(width=100, height=80, color=(128, 128, 128), fmt='jpg'):
    import cv2
    img = np.full((height, width, 3), color, dtype=np.uint8)
    ext = f'.{fmt}'
    fd, path = tempfile.mkstemp(suffix=ext)
    os.close(fd)
    if fmt == 'jpg':
        cv2.imwrite(path, img, [cv2.IMWRITE_JPEG_QUALITY, 95])
    else:
        cv2.imwrite(path, img)
    return _register(path)


def make_blank_image(width=100, height=80, fmt='jpg'):
    return make_test_image(width, height, (255, 255, 255), fmt)


def make_corrupted_file():
    fd, path = tempfile.mkstemp(suffix='.jpg')
    os.write(fd, b'\x00\x00\x00\x00\x00\x00\x00\x00')
    os.close(fd)
    return _register(path)


def make_empty_file():
    fd, path = tempfile.mkstemp(suffix='.jpg')
    os.close(fd)
    return _register(path)


def make_blurry_image():
    import cv2
    img = np.full((200, 200, 3), 128, dtype=np.uint8)
    img = cv2.GaussianBlur(img, (99, 99), 30)
    fd, path = tempfile.mkstemp(suffix='.jpg')
    os.close(fd)
    cv2.imwrite(path, img, [cv2.IMWRITE_JPEG_QUALITY, 10])
    return _register(path)


def make_sharp_image():
    import cv2
    img = np.random.randint(0, 255, (300, 300, 3), dtype=np.uint8)
    kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
    img = cv2.filter2D(img, -1, kernel)
    fd, path = tempfile.mkstemp(suffix='.jpg')
    os.close(fd)
    cv2.imwrite(path, img, [cv2.IMWRITE_JPEG_QUALITY, 95])
    return _register(path)


def make_face_image():
    """Create a simple face-like pattern"""
    img = np.full((200, 200, 3), 200, dtype=np.uint8)
    cv2.circle(img, (100, 80), 50, (180, 160, 140), -1)
    cv2.circle(img, (80, 70), 8, (50, 50, 50), -1)
    cv2.circle(img, (120, 70), 8, (50, 50, 50), -1)
    cv2.circle(img, (100, 95), 5, (80, 60, 60), -1)
    fd, path = tempfile.mkstemp(suffix='.jpg')
    os.close(fd)
    cv2.imwrite(path, img)
    return _register(path)
