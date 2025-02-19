# Original package name LuaExpat
%define oname luaexpat
%define oversion 1.3.0-1
%define rockspec %oname-%oversion.rockspec
Name: lua-module-%oname
Version: 1.3.0
Release: alt2
Summary: XML Expat parsing
License: MIT/X11
Group: Development/Other
Url: http://www.keplerproject.org/luaexpat/
Packager: Ildar Mulyukov <ildar@altlinux.ru>
Obsoletes: lua5-luaexpat
Provides: lua5-luaexpat = %version
Provides: luarocks(%oname) = %version

Source: http://matthewwild.co.uk/projects/luaexpat/luaexpat-1.3.0.tar.gz
Source1: https://rocks.moonscript.org/manifests/luarocks/luaexpat-1.3.0-1.rockspec

BuildPreReq: rpm-macros-lua >= 1.2
# Automatically added by buildreq on ...
BuildRequires: liblua5-devel luarocks
BuildRequires: libexpat-devel

%description
      LuaExpat is a SAX (Simple API for XML) XML parser based on the
      Expat library.

%prep
%setup -n %oname-%version

%install
%luarocks_make %SOURCE1
%luarocks_move_docs doc

%check
%lua_path_add_buildroot
for t in %buildroot%luarocks_dbdir/%oname/%oversion/tests/* ; do
  lua $t
done

%files
%lua_modulesdir/*
%lua_modulesdir_noarch/*
%luarocks_dbdir/%oname
%doc README* docs_from_rockstree/*
%exclude %luarocks_dbdir/manifest

%changelog
* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.3.0-alt2
- Rebuild with new luarocks and lua-5.3

* Mon Oct 06 2014 Ildar Mulyukov <ildar@altlinux.ru> 1.3.0-alt1_lr1
- autogenerated by lrimport

