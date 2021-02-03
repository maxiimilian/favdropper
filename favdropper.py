import sys
from typing import List
import os
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QLineEdit,
    QPlainTextEdit,
    QLabel,
    QFileDialog,
)


class FavDropperMain(QWidget):
    def __init__(self):
        super().__init__()

        self._target_directory: QtCore.QUrl = QtCore.QUrl("")

        self.setAcceptDrops(True)
        self.init_ui()

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        if e.mimeData().hasUrls():
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        # Filter local files (i.e. file:///)
        urls = [
            u
            for u in e.mimeData().urls()
            if u.isLocalFile()
        ]

        if len(urls) > 0:
            # If target dir not yet set, use input for that
            if self.target_directory.path() == "":
                target_directory = urls[0]
                if os.path.isdir(target_directory.path()):
                    self.target_directory = target_directory
            else:
                self.link_urls(urls)

    @property
    def target_directory(self) -> QtCore.QUrl:
        return self._target_directory

    @target_directory.setter
    def target_directory(self, value: QtCore.QUrl):
        self._target_directory = value
        self._target_txt.setText(value.toString())
        self._log.appendPlainText(
            "Target directory selected."
        )

    def init_ui(self):
        # Set up controls
        self._target_btn = QPushButton("Select")
        self._target_btn.clicked.connect(self.pick_target_dir)
        self._target_txt = QLineEdit()
        self._target_txt.setDisabled(True)

        # Set up directory picker
        self._h_box = QHBoxLayout()
        self._h_box.addStretch(1)
        self._h_box.addWidget(QLabel(
            "Target directory"
        ))
        self._h_box.addWidget(self._target_txt)
        self._h_box.addWidget(self._target_btn)

        # Set up drop area
        self._file_drop_label = QLabel("Please drop files to be linked here")

        # Set up log
        self._log = QPlainTextEdit()
        self._log.setReadOnly(True)

        # Set up main layout
        v_box = QVBoxLayout()
        v_box.addStretch(1)
        v_box.addLayout(self._h_box)
        v_box.addWidget(self._file_drop_label)
        v_box.addWidget(self._log)

        self.setLayout(v_box)
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('FavDropper')
        self.show()

    def pick_target_dir(self) -> None:
        """
        Opens file dialog to pick target directory for links
        """
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.DirectoryOnly)

        if dlg.exec_():
            self.target_directory = dlg.selectedUrls()[0]

    def link_urls(self, urls: List[QtCore.QUrl]) -> None:
        for u in urls:
            rel_u = os.path.relpath(
                u.path(),
                self.target_directory.path()
            )
            target_u = os.path.join(
                self.target_directory.path(),
                u.fileName()
            )

            try:
                os.symlink(rel_u, target_u)
                msg = f"{u.fileName()} linked!"
            except FileExistsError:
                msg = f"{u.fileName()} already exists in destination! Skipping."
            self._log.appendPlainText(msg)


def main():
    app = QApplication(sys.argv)
    main = FavDropperMain()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()