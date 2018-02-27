Name: bindfs
Version: 1.12.1
Release: alt1
License: GPLv2
Summary: %name is a FUSE filesystem for mounting a directory to another location, similarly to mount --bind
Group: System/Base
Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>
URL: http://code.google.com/p/bindfs/
Source: %name-%version.tar.gz

BuildRequires: libfuse-devel

%description
bindfs is a FUSE filesystem for mounting a directory to another location, similarly to mount --bind.
The permissions inside the mountpoint can be altered using various rules.

%prep
%setup

%build
%autoreconf
%configure
%make

%install
%makeinstall_std

%files
%doc COPYING ChangeLog README TODO
%_bindir/*
%_man1dir/*

%changelog
* Sat May 11 2013 Slava Dubrovskiy <dubrsl@altlinux.org> 1.12.1-alt1
- New version

* Sat Nov 17 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 1.11-alt1
- New version

* Tue Nov 15 2011 Slava Dubrovskiy <dubrsl@altlinux.org> 1.9-alt1
- Build for ALT
