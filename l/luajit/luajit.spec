Name: luajit
Version: 2.0.4
Release: alt1

Summary: a Just-In-Time Compiler for Lua
License: MIT
Group: Development/Other
Url: http://luajit.org
Packager: Vladimir Didenko <cow@altlinux.org>
# git://git.altlinux.org/gears/l/luajit.git
Source: %name-%version.tar
Patch: %name-2.0.4-alt-luadir-path.patch
Requires: lib%name = %EVR

%description
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language.
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name
Summary: library for luajit
Group: Development/Other

%description -n lib%name
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language.
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name-devel
Summary:  Development package that includes the luajit header files
Group: Development/Other
Requires: lib%name = %EVR

%description -n lib%name-devel
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language.
It may be embedded or used as a general-purpose, stand-alone language.

%package -n lib%name-devel-static
Summary: static library for luajit
Group: System/Libraries
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
LuaJIT is a Just-In-Time Compiler (JIT) for the Lua programming language.
Lua is a powerful, dynamic and light-weight programming language.
It may be embedded or used as a general-purpose, stand-alone language.

%prep
%setup
%patch -p1

%ifarch x86_64
%define multilib_flag lib64
%else
%define multilib_flag lib
%endif

%build
%make_build amalg \
	    PREFIX=%_prefix \
	    MULTILIB=%multilib_flag \
	    TARGET_STRIP='@:' \
	    Q=

%install
%makeinstall_std PREFIX=%_prefix \
		 MULTILIB=%multilib_flag \
		 INSTALL_LMOD=%buildroot%_datadir/lua5 \
		 INSTALL_CMOD=%buildroot%_libdir/lua5 \
		 LDCONFIG=true \
		 INSTALL_LIB=%buildroot%_libdir \
		 Q=

%files
%_bindir/*
%_man1dir/*

%files -n lib%name
%_libdir/*.so.*
%_datadir/%name-*

%files -n lib%name-devel
%doc doc/*
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Sat May 16 2015 Vladimir Didenko <cow@altlinux.org> 2.0.4-alt1
- 2.0.4

* Tue Feb 24 2015 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt6
- git20150222

* Wed Feb 18 2015 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt5
- use the same path and cpath as plain lua (closes: #30739)

* Mon Jan 12 2015 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt4
- git20150105

* Wed Sep 10 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt3
- git20140908

* Fri Jul 4 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt2
- git20140701

* Thu Mar 20 2014 Vladimir Didenko <cow@altlinux.org> 2.0.3-alt1
- new version

* Sun Apr 14 2013 Dmitry V. Levin <ldv@altlinux.org> 2.0.1-alt1
- NMU: updated v2.0.1-fixed-14-gb1327bc, fixed build.

* Sun Dec 16 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.0-alt1
- Build for ALT
