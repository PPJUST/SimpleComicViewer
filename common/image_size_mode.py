# 图片大小模式（固定宽度/适合页面/适合宽度/适合高度/实际大小）

class ImageSizeMode:
    """图片大小模式"""

    class Fixed:
        """固定宽度"""
        pass

    class FitPage:
        """适合页面"""
        pass

    class FitHeight:
        """适合高度"""
        pass

    class FitWidth:
        """适合宽度"""
        pass

    class FullSize:
        """实际大小"""
        pass
