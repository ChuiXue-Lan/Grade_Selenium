import os


class Functions:

    # SET SVG ICON
    def set_svg_icon(icon_name):
        # 获取当前绝对路径
        app_path = os.path.abspath(os.getcwd())
        folder = "images/svg_icons/"
        path = os.path.join(app_path, folder)
        # 规范化路径，以确保路径在不同操作系统上的正确性。
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET SVG IMAGE
    def set_svg_image(icon_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "images/svg_images/"
        path = os.path.join(app_path, folder)
        icon = os.path.normpath(os.path.join(path, icon_name))
        return icon

    # SET IMAGE
    def set_image(image_name):
        app_path = os.path.abspath(os.getcwd())
        folder = "images/images/"
        path = os.path.join(app_path, folder)
        image = os.path.normpath(os.path.join(path, image_name))
        return image