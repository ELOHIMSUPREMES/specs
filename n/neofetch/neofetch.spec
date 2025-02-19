%define _unpackaged_files_terminate_build 1

Name: neofetch
Version: 6.0.0
Release: alt1

Summary: A command-line system information tool
License: MIT
Group: Monitoring

URL: https://github.com/dylanaraps/neofetch
Source: %name-%version.tar

BuildArch: noarch

%description
Neofetch is a command-line system information tool written in bash 3.2+.
Neofetch displays information about your operating system, software and
hardware in an aesthetic and visually pleasing way.


%prep
%setup

%build

%install
%makeinstall_std

%files
%_bindir/%name
%_man1dir/%name.1.xz

%changelog
* Sun Mar 31 2019 Alexander Makeenkov <amakeenk@altlinux.org> 6.0.0-alt1
- Initial build for ALT

