# 更多选项dialog

from PySide6.QtCore import Signal
from PySide6.QtWidgets import *

from module import function_config
from ui.ui_src.ui_dialog_option import Ui_Dialog


class DialogOption(QDialog):
    """更多选项dialog"""
    signal_option_changed = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # 加载设置
        self._load_setting()

        # 设置槽函数
        self.ui.pushButton_confirm.clicked.connect(self._confirm)
        self.ui.pushButton_cancel.clicked.connect(self.close)

    def _load_setting(self):
        """加载设置"""
        self.ui.checkBox_skip_solid_color_page.setChecked(
            function_config.GetSetting.skip_solid_color_page())
        self.ui.checkBox_sharpen_image.setChecked(
            function_config.GetSetting.sharpen_image())
        self.ui.spinBox_preload_pages.setValue(
            function_config.GetSetting.preload_pages())
        self.ui.comboBox_switch_page_mode.addItems(
            function_config.GetSetting.switch_page_modes())
        self.ui.comboBox_switch_page_mode.setCurrentText(
            function_config.GetSetting.current_switch_page_mode())

    def _confirm(self):
        """确认"""
        function_config.ResetSetting.skip_solid_color_page(
            self.ui.checkBox_skip_solid_color_page.isChecked())
        function_config.ResetSetting.sharpen_image(
            self.ui.checkBox_sharpen_image.isChecked())
        function_config.ResetSetting.current_switch_page_mode(
            self.ui.comboBox_switch_page_mode.currentText())
        function_config.ResetSetting.preload_pages(
            self.ui.spinBox_preload_pages.value())
        self.signal_option_changed.emit()
        self.close()
