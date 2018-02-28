
Name:		pdfchain
Version:	0.4.4
Release:	alt2

Summary:	A graphical user interface for the PDF Toolkit (PDFtk)
Group:		Office
License:	GPLv3+
URL:		http://sourceforge.net/projects/pdfchain
Source0:	http://downloads.sourceforge.net/pdfchain/%{name}-%{version}.tar.gz

BuildRequires:	gcc-c++
BuildRequires:	libgtkmm3-devel
BuildRequires:	intltool

Requires:	pdftk

%description
PDF Chain is a GUI for pdftk written with gtkmm. You can merge some pdf
files to one pdf file or split. There are also some options and tools.

%prep
%setup -q
# Stop if files acquire content
[ -s NEWS ] && exit 1

%build
%add_optflags -std=c++11
%configure
%make_build

%install
%makeinstall_std

# Remove doc dir
rm -rf %buildroot%_docdir/pdfchain

%files
%doc AUTHORS ChangeLog NEWS README
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_pixmapsdir/%name.png

%changelog
* Tue Oct 06 2015 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt2
- Fix build with c++11

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.4.4-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Nov 21 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.4-alt1
- New version

* Thu Nov 21 2013 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1
- Initial import from Fedora
