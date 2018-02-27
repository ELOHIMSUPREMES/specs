Name: irextools
Version: 0.3
Release: alt2

Summary: PDF merge and metadata support tools for iRex DR1000 e-ink devices
Summary (ru_RU.UTF-8): Объединение PDF и заметок и поддержка метаданных для устройств iRex DR1000
License: GPL
Group: Office
URL: http://forge.ocamlcore.org/projects/irextools/
Source: http://forge.ocamlcore.org/frs/download.php/108/irextools-0.3.tar.gz

BuildRequires: rpm-build-ocaml4 ocaml4-camlp4 ocaml4-ocamldoc libsqlite3-devel libtinfo-devel zlib-devel

Packager: Slava <slava@altlinux.ru>

%description
A free and portable set of tools for the iRex Digital Reader 1000S. 
The most important part is a flexible tool for merging handwritten notes with 
PDF files. Other tools aid in the maintenance of metadata associated with 
the documents.

%description -l ru_RU.UTF-8
Свободный и независимый от конкретной ОС набор утилит для iRex Digital Reader 1000S.
Наиболее важным инстрментом является программа для объединения рукописных заметок, 
сделанных стилусом на полях или поверх текста, с исходным PDF. Остальные функции
предназначены для работы с метаданными документов.

%prep
%setup -q

%build
%configure
%make_build

bzip2 -9 ism.1
bzip2 -9 irext.1

%install
#make_install
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot%_man1dir
%__install -pD -m755 ism %buildroot%_bindir/ism
%__install -pD -m755 irext %buildroot%_bindir/irext
%__install -pD -m644 ism.1.bz2 %buildroot%_man1dir/ism.1.bz2
%__install -pD -m644 irext.1.bz2 %buildroot%_man1dir/irext.1.bz2

%files
%_bindir/ism
%_bindir/irext
%_man1dir/ism*
%_man1dir/irext*
%doc README TODO

%changelog
* Wed Jun 24 2015 Andrey Bergman <vkni@altlinux.org> 0.3-alt2
- Rebuilt with Ocaml4, added man page compression.

* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.3-alt1.qa1
- NMU: rebuilt for debuginfo.

* Sun Jan 18 2009 Vyacheslav Dikonov <slava@altlinux.ru> 0.3-alt1
- ALTLinux build
