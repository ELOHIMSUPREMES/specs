# %%define _unpackaged_files_terminate_build 1

Name:       exe
Version:    2.3.1
Release:    alt1
BuildArch:  noarch

License:    %gpl2plus
Group:      Education
Summary:    Tool to create and publish open educational resources.

Url:        http://exelearning.net
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-licenses
BuildRequires: desktop-file-utils
BuildRequires: python-module-glob2
BuildRequires: python-module-distutils-extra

Requires: python-module-%name = %EVR

%add_python_req_skip AppKit Carbon Foundation GDK
%add_python_req_skip PAM SOAPpy cfsupport
%add_python_req_skip kqsyscall msvcrt pythoncom
%add_python_req_skip pyui pyunit pywintypes qt
%add_python_req_skip win32api win32com win32con
%add_python_req_skip win32event win32file win32gui
%add_python_req_skip win32pipe win32process win32security


%description
This authoring environment enables teachers and students to create and publish
educational content without the need to become proficient in HTML or XML markup.
Content generated using eXeLearning can be exported as web pages, as
educational-standard packages used by any Learning Management System, as epub3
files and on mobile devices.

%package -n python-module-%name
License:    %gpl2plus
Group:      Development/Python
Summary:    Python modules for eXeLearning.
BuildArch:  noarch

Requires: mimetex
Requires: python-module-lxml
Requires: python-module-Pillow
Requires: python-module-zope.interface

%description -n python-module-%name
This authoring environment enables teachers and students to create and publish
educational content without the need to become proficient in HTML or XML markup.
Content generated using eXeLearning can be exported as web pages, as
educational-standard packages used by any Learning Management System, as epub3
files and on mobile devices.

Package contains python modules for eXeLearning.

%prep
%setup -n %name

%build
%python_build

%install
%python_install

rm -rf %buildroot%_datadir/%name/formless 
rm -rf %buildroot%_datadir/%name/templates/*.cgi 
rm -rf %buildroot%_datadir/%name/templates/*.exe
rm -rf %buildroot%_datadir/%name/twisted/internet/cfsupport
rm -rf %buildroot%_datadir/%name/twisted/internet/iocpreactor

ln -s %_var/www/cgi-bin/mimetex.cgi %buildroot%_datadir/%name/templates/

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete
desktop-file-install --dir %buildroot%_desktopdir \
    --remove-category=Editor \
    --remove-category=Application \
    --add-category=TextEditor \
    %buildroot%_desktopdir/exe.desktop

mkdir -p %buildroot%_datadir/mime/packages/
cp exe.xml %buildroot%_datadir/mime/packages/

%files
%dir %_datadir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_bindir/%{name}*
%_datadir/locale/*/LC_MESSAGES/exe.mo

%files -n python-module-%name
%python_sitelibdir/%{name}*


%changelog
* Mon Feb 25 2019 Andrey Bychkov <mrdrew@altlinux.org> 2.3.1-alt1
- Version updated to 2.3.1

* Thu Mar 15 2018 Igor Vlasenko <viy@altlinux.ru> 1.04.0.3532-alt1.qa3
- NMU: added URL

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.04.0.3532-alt1.qa2.1
- Rebuild with Python-2.7

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 1.04.0.3532-alt1.qa2
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for exe

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.04.0.3532-alt1.qa1.1
- Rebuilt with python 2.6

* Sat Nov 14 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.04.0.3532-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * windows-thumbnail-database-in-package for exe
  * postclean-05-filetriggers for spec file

* Sat Aug 29 2009 Fr. Br. George <george@altlinux.ru> 1.04.0.3532-alt1
- Initial build freom scratch

