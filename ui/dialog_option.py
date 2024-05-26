# 选项dialog
# 备忘录 边框设置
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog

from module.function_config_get import GetSetting
from module.function_config_reset import ResetSetting
from ui.ui_src.ui_dialog_option import Ui_Dialog


class DialogOption(QDialog):
    """选项dialog"""
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

        # 屏蔽未完成的选项
        self.ui.checkBox_sharpen_image.setEnabled(False)
        self.ui.checkBox_skip_solid_color_page.setEnabled(False)
        self.ui.comboBox_switch_page_mode.setEnabled(False)

    def _load_setting(self):
        """加载设置"""
        self.ui.checkBox_skip_solid_color_page.setChecked(GetSetting.skip_solid_color_page())
        self.ui.checkBox_sharpen_image.setChecked(GetSetting.sharpen_image())
        self.ui.spinBox_preload_pages.setValue(GetSetting.preload_pages())
        self.ui.comboBox_switch_page_mode.addItems(GetSetting.switch_page_modes())
        self.ui.comboBox_switch_page_mode.setCurrentText(GetSetting.current_switch_page_mode())

    def _confirm(self):
        """确认"""
        ResetSetting.skip_solid_color_page(self.ui.checkBox_skip_solid_color_page.isChecked())
        ResetSetting.sharpen_image(self.ui.checkBox_sharpen_image.isChecked())
        ResetSetting.current_switch_page_mode(self.ui.comboBox_switch_page_mode.currentText())
        ResetSetting.preload_pages(self.ui.spinBox_preload_pages.value())
        self.signal_option_changed.emit()
        self.close()
