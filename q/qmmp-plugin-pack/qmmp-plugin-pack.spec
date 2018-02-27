%define		branch 0.8
%define		svn svn3984

Version:	%branch.0.1
Name:		qmmp-plugin-pack
Release:	alt1.%svn
Summary:	Plugin pack is a set of extra plugins for Qmmp.
Summary(ru_RU.UTF8): Набор дополнительных модулей для Qmmp.
Summary(uk_UA.UTF8): Набір додаткових модулів для Qmmp.
License:	GPLv2
Group:		Sound
Packager:	Motsyo Gennadi <drool@altlinux.ru>
Url:		http://qmmp.ylsoftware.com/plugins_en.php
Source0:	%name-%branch-%svn.tar.bz2


BuildRequires:	libqt4-devel gcc-c++ libmpg123-devel libqmmp-devel >= %branch libtag-devel >= 1.6 yasm

%description
Plugin pack is a set of extra plugins for Qmmp.

Plugins List
 - MPG123 - MPEG v1/2 layer1/2/3 decoder using of libmpg123 library
 - FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support)
 - Qmmp Simple Ui (QSUi) - simple user interface based on standard widgets set

%description -l ru_RU.UTF8
Набор дополнительных модулей для Qmmp.

Список модулей
 - MPG123 - декодер MPEG v1/2 layer1/2/3 с использованием библиотеки libmpg123
 - FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue)
 - Qmmp Simple Ui (QSUi) - простой пользовательский интерфейс с использованием стандартных элементов

%description -l uk_UA.UTF8
Набір додаткових модулів для Qmmp.

Перелік модулів
 - MPG123 - декодер MPEG v1/2 layer1/2/3 з використанням бібліотеки libmpg123
 - FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue)
 - Qmmp Simple Ui (QSUi) - простий інтерфейс користувача з використанням стандартних елементів

%package -n %name-in-mpg123
Summary: MPG123 - MPEG v1/2 layer1/2/3 decoder using of libmpg123 library
Summary(ru_RU.UTF8): MPG123 - декодер MPEG v1/2 layer1/2/3 с использованием библиотеки libmpg123
Summary(uk_UA.UTF8): MPG123 - декодер MPEG v1/2 layer1/2/3 з використанням бібліотеки libmpg123
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-in-mpg123
MPG123 - MPEG v1/2 layer1/2/3 decoder using of libmpg123 library for Qmmp.

%description -l ru_RU.UTF8 -n %name-in-mpg123
MPG123 - декодер MPEG v1/2 layer1/2/3 с использованием библиотеки libmpg123 для Qmmp.

%description -l uk_UA.UTF8 -n %name-in-mpg123
MPG123 - декодер MPEG v1/2 layer1/2/3 з використанням бібліотеки libmpg123 для Qmmp.

%package -n %name-in-ffap
Summary: FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support)
Summary(ru_RU.UTF8): FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue)
Summary(uk_UA.UTF8): FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue)
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-in-ffap
FFap - enhanced Monkey's Audio (APE) decoder (24-bit samples and embedded cue support) for Qmmp.

%description -l ru_RU.UTF8 -n %name-in-ffap
FFap - улучшенный декодер Monkey's Audio (APE) (поддержка 24-х бит и встроенного cue) для Qmmp.

%description -l uk_UA.UTF8 -n %name-in-ffap
FFap - покращений декодер Monkey's Audio (APE) (підтримка 24-х біт та вбудованого cue) для Qmmp.

%package -n %name-qsui
Summary: Qmmp Simple Ui - simple user interface based on standard widgets set
Summary(ru_RU.UTF8): Qmmp Simple Ui - простой пользовательский интерфейс с использованием стандартных элементов
Summary(uk_UA.UTF8): Qmmp Simple Ui - простий інтерфейс користувача з використанням стандартних елементів
Group: Sound
Requires: qmmp >= %version-%release

%description -n %name-qsui
Qmmp Simple Ui - simple user interface based on standard widgets set for Qmmp.

%description -l ru_RU.UTF8 -n %name-qsui
Qmmp Simple Ui - простой пользовательский интерфейс с использованием стандартных элементов для Qmmp.

%description -l uk_UA.UTF8 -n %name-qsui
Qmmp Simple Ui - простий інтерфейс користувача з використанням стандартних елементів для Qmmp.

%prep
%setup -q -n %name-svn

%build
export PATH=$PATH:%_qt4dir/bin
qmake-qt4 "QMAKE_CFLAGS+=%optflags" "QMAKE_CXXFLAGS+=%optflags" LIB_DIR=/%_lib %name.pro
%make_build VERBOSE=1

%install
%make INSTALL_ROOT=%buildroot%prefix install

%files -n %name-in-mpg123
%_libdir/qmmp/Input/libmpg123.so

%files -n %name-in-ffap
%_libdir/qmmp/Input/libffap.so

%files -n %name-qsui
%_libdir/qmmp/Ui/libqsui.so

%changelog
* Wed Dec 25 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn3984
- build svn3984

* Sat Nov 23 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0.1-alt1.svn3924
- build svn3924

* Thu Nov 14 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3910
- build svn3910

* Thu Nov 07 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3880
- build svn3880

* Fri Oct 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3815
- build svn3815

* Mon Aug 26 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3669
- build svn3669

* Thu Aug 22 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3647
- build svn3647

* Tue Aug 20 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3630
- build svn3630

* Thu Jul 18 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3555
- build svn3555

* Tue May 21 2013 Motsyo Gennadi <drool@altlinux.ru> 0.8.0-alt1.svn3479
- build svn3479

* Wed Jan 16 2013 Motsyo Gennadi <drool@altlinux.ru> 0.7.0-alt1.svn3169
- build svn3169

* Tue Dec 18 2012 Motsyo Gennadi <drool@altlinux.ru> 0.7.0-alt1.svn3077
- build svn3077

* Mon Jul 16 2012 Motsyo Gennadi <drool@altlinux.ru> 0.6.0-alt1.svn2810
- initial build for ALT Linux
