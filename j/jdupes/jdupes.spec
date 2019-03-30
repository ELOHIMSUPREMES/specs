Name: jdupes
Version: 1.12
Release: alt1

Summary: A powerful duplicate file finder and an enhanced fork of 'fdupes'

License: %mit
Group: File tools
Url: https://github.com/jbruchon/jdupes

# Source-url: https://github.com/jbruchon/jdupes/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-build-licenses

%description
jdupes is a program for identifying and taking actions upon duplicate
files.

A WORD OF WARNING: jdupes IS NOT a drop-in compatible replacement for
fdupes! Do not blindly replace fdupes with jdupes in scripts and expect
everything to work the same way. Option availability and meanings differ
between the two programs. For example, the -I switch in jdupes means
"isolate" and blocks intra-argument matching, while in fdupes it means
"immediately delete files during scanning without prompting the user."

%prep
%setup

%build
%make_build

%install
%makeinstall PREFIX=%buildroot%prefix MAN_BASE_DIR=%buildroot%_mandir CFLAGS_EXTRA="%optflags" install

%check
./jdupes testdir
./jdupes -r testdir

%files
%doc CHANGES README
%_bindir/*
%_man1dir/*

%changelog
* Sat Mar 30 2019 Vitaly Lipatov <lav@altlinux.ru> 1.12-alt1
- initial build for ALT Sisyphus


