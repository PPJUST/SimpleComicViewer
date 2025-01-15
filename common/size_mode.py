# 显示模式（适合页面/适合宽度/适合高度/实际大小）

class PageSizeMode:
    """显示模式"""


    class FitPage:
        """适合页面"""
        pass

    class FitHieght:
        """适合高度"""
        pass

    class FitWidth:
        """适合宽度"""
        pass

    class FullSize:
        """实际大小"""
        pass

    def get_current_mode(self):
        """获取当前显示模式"""