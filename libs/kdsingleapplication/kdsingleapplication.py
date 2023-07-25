import io
import os
import re

import info


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ["1.0.0"]:
            self.targets[ver] = f"https://github.com/KDAB/KDSingleApplication/releases/download/v{ver}/kdsingleapplication-{ver}.tar.gz"
            self.targetInstSrc[ver] = "kdsingleapplication-1.0.0"
        self.svnTargets["master"] = "https://github.com/KDAB/KDSingleApplication.git"

        self.targetDigests["1.0.0"] = (["c92355dc10f3ebd39363458458fb5bdd9662e080cf77d91f0437763c4d936520"], CraftHash.HashAlgorithm.SHA256)
        self.defaultTarget = "1.0.0"

        self.description = "KDSingleApplication is a helper class for single-instance policy applications written by KDAB."
        self.webpage = "https://github.com/KDAB/KDSingleApplication"

    def setDependencies(self):
        self.buildDependencies["craft/craft-blueprints-owncloud"] = None
        self.runtimeDependencies["libs/qt/qtbase"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        if self.subinfo.options.dynamic.buildTests:
            self.subinfo.options.configure.args += ["-DKDSingleApplication_TESTS=ON"]
        if CraftPackageObject.get("libs/qt").instance.subinfo.options.dynamic.qtMajorVersion == "6":
            self.subinfo.options.configure.args += ["-DKDSingleApplication_QT6=ON"]
