Name: wxlua
Version: 2.8.12.3
Release: alt3.r246.1
Summary: Lua IDE with a GUI debugger and binding generator
License: wxWidgets License
Group: Development/Other
Url: http://wxlua.sourceforge.net/
Packager: Ildar Mulyukov <ildar@altlinux.ru>

# svn://svn.code.sf.net/p/wxlua/svn/trunk
Source: http://sourceforge.net/projects/wxlua/files/wxlua/%version/wxLua-%version-src.tar
#.gz

# Automatically added by buildreq on Thu Oct 09 2014 (-bi)
# optimized out: cmake-modules elfutils fontconfig libGL-devel libX11-devel libcloog-isl4 libgdk-pixbuf libgst-plugins libstdc++-devel libwayland-client libwayland-server libwxGTK-contrib-stc python-base xorg-xproto-devel
BuildRequires: cmake desktop-file-utils gcc-c++ libGLU-devel liblua5-devel libwxGTK3.1-devel libwxstedit-devel lua5
#BuildRequires: doxygen graphviz

%description
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

Additionally, wxLua can be used in your C++ programs to embed a Lua interpreter with the wxWidgets API.

This package contains Integrated Development Environments (IDE, written in
wxLua) with a GUI debugger, a binding generator and wxWidgets bindings usable
as a module.

%package -n lib%name
Group: System/Libraries
Summary: set of Lua bindings to the C++ wxWidgets cross-platform GUI library

%description -n lib%name
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

%package -n lib%name-devel
Group: Development/C++
Summary: Development files of lib%name
Requires: lib%name = %version-%release

%description -n lib%name-devel
wxLua is a set of bindings to the C++ wxWidgets cross-platform GUI library for
the Lua programming language. Nearly all of the functionality of wxWidgets is
exposed to Lua, meaning that your programs can have windows, dialogs, menus,
toolbars, controls, image loading and saving, drawing, sockets, streams,
printing, clipboard access... and much more.

This package contains files required for compiling and linking
applications with lib%name.

%if_enabled static
%package -n lib%name-devel-static
Group: Development/C++
Summary: Static library of %name
Requires: %name-devel = %version-%release

%description -n lib%name-devel-static
This package contains the static library required for statically linking
applications with %name.

%endif #enabled static

%prep
%setup -n wxLua-%version-src
rm -rf modules/{lua-*,wxstedit}/*
sed -r -i 's|LIBRARY DESTINATION .*$|LIBRARY DESTINATION %_lib|' \
	CMakeLists.txt

# prepare external wxstedit
ln -s /usr/include modules/wxstedit
echo "project( wxStEdit )" > modules/wxstedit/CMakeLists.txt

%build
%cmake \
	-DwxLua_LUA_LIBRARY_USE_BUILTIN=FALSE \
	-DwxStEdit_ROOT_DIR=$PWD/modules/wxstedit

pushd bindings
	make clean all \
		LUA=%_bindir/lua
popd
%make_build -C BUILD
if [ -x /usr/bin/doxygen ]; then
	%make_build -C BUILD wxLua_doxygen
fi

%install
%makeinstall_std -C BUILD

mkdir -p \
	%buildroot%_desktopdir/ \
	%buildroot%_libdir/lua5/ \
	%buildroot%_iconsdir/hicolor/scalable/apps/
install -p art/wxlualogo.svg %buildroot%_iconsdir/hicolor/scalable/apps/
mv %buildroot%_libdir/libwx.so %buildroot%_libdir/lua5/wx.so
install -p distrib/autopackage/%name.desktop %buildroot%_desktopdir/
sed -r -i "s|wxluaedit|wxLuaEdit|" %buildroot%_desktopdir/%name.desktop
desktop-file-install --dir %buildroot%_desktopdir \
	--remove-category=Application \
	--add-category=IDE \
	%buildroot%_desktopdir/%name.desktop

%files
%_bindir/*
%_desktopdir/*.desktop
%_iconsdir/hicolor/scalable/apps/*
%_datadir/%name
%doc docs/*

%files -n lib%name
%_libdir/*.so
%_libdir/lua5/*.so

%files -n lib%name-devel
%_includedir/%name
#%%doc BUILD/doc-wxLua/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Sat Jan 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.12.3-alt3.r246.1
- Built with updated wxGTK3.1

* Mon Oct 27 2014 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt3.r246
- build with wxGTK3.1 + GTK+3
- fixed upstream

* Wed Oct 15 2014 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt2.r244
- SVN version
- build with libwxGTK3.0-devel

* Wed Oct 08 2014 Ildar Mulyukov <ildar@altlinux.ru> 2.8.12.3-alt1
- new version

* Tue Jan 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.10.0-alt1.qa4
- Rebuilt with wxGTK 2.8.12

* Wed Jun 20 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.10.0-alt1.qa3
- Fixed build with gcc 4.6

* Sat Dec 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.8.10.0-alt1.qa2

* Tue May 24 2011 Repocop Q. A. Robot <repocop@altlinux.org> 2.8.10.0-alt1.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for wxlua

* Thu Jun 17 2010 Ildar Mulyukov <ildar@altlinux.ru> 2.8.10.0-alt1
- initial build for ALTLinux
- disabled wxGTK Media binding
