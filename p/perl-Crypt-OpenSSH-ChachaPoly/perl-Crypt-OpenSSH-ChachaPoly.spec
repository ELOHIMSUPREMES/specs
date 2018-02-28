%define dist Crypt-OpenSSH-ChachaPoly

%define _unpackaged_files_terminate_build 1

Name: perl-%dist
Version: 0.02
Release: alt1

Summary: This module serves as a wrapper to the OpenSSH Chacha20 and Poly1305 functions
License: %perl_license
Group: Development/Perl

URL: http://github.com/lkinley/Crypt-OpenSSH-ChachaPoly
Source: %dist-%version.tar.gz

BuildRequires: rpm-build-licenses

# Automatically added by buildreq on Thu Feb 18 2016
BuildRequires: perl-Encode perl-devel

%description
This module serves as a wrapper to the OpenSSH Chacha20 and Poly1305 functions

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Crypt
%perl_vendor_autolib/Crypt

%changelog
* Thu Apr 21 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.02-alt1
- new version

* Thu Feb 18 2016 Sergey Y. Afonin <asy@altlinux.ru> 0.01-alt1
- initial build
