# SPEC file for the BetterPrivacy Firefox extension

%define rname	betterprivacy
%define version	1.68
%define release	alt1
%define cid	\{d40f5e7b-d2cf-4856-b441-cc613eeffbe3\}
%define ciddir	%firefox_noarch_extensionsdir/%cid

Name:		%firefox_name-%rname
Version:	%version
Release:	%release

Summary:	BetterPrivacy Firefox extension
Summary(ru_RU.UTF-8):	расширение BetterPrivacy для Firefox

License:	%mpl 1.1
Group:		Networking/WWW
URL:		https://addons.mozilla.org/ru/firefox/addon/betterprivacy/
BuildArch:      noarch

Source0:	%rname.xpi
Packager:	Nikolay A. Fetisov <naf@altlinux.ru>

BuildRequires(pre):	rpm-build-firefox rpm-build-licenses
BuildRequires:		unzip

%description
BetterPrivacy Firefox extension remove or manage an LSO
(Local Shared Objects) Flash cookies.
The BetterPrivacy safeguard offers various ways to handle
Flash-cookies set by Google, YouTube, Ebay and others...

%description -l ru_RU.UTF-8
Расширение BetterPrivacy для Firefox позволяет удалять
объекты LSO (Local Shared Objects) дополнения Flash
(flash-cookies).

Объекты LSO используются для отслеживания активности
пользователей многими сайтами, в т.ч. их использует Google,
YouTube, Ebay, VK, и т.д. В отличие от обычных cookies
LSO являются браузеро-независимыми, хранятся постоянно,
и стандартными средствами браузеров не показываются.


%prep
%setup -c

# RPM call unzip with -Lq keys, effectivly kills all mixed-case filenames in archive
rm -rf -- ./*
unzip -q %SOURCE0

%install
mkdir -p -- %buildroot/%ciddir
cp -r -- * %buildroot/%ciddir

%postun
if [ "$1" = 0 ]; then
  [ ! -d "%ciddir" ] || rm -rf "%ciddir"
fi

%files
%ciddir

%changelog
* Tue Jun 11 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.68-alt1
- Initial build for ALT Linux Sisyphus
