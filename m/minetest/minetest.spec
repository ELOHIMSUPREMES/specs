%define _hardened_build 1
%global gitname celeron55

Name:		minetest
Version:	0.4.7
Release:	alt1
Summary:	Multiplayer infinite-world block sandbox with survival mode

Group:		Games/Other
License:	LGPLv2+ and CC-BY-SA
URL:		http://minetest.net/index.php

# curl -L -O http://github.com/celeron55/minetest/tarball/0.4.3/minetest-0.4.3.tar.gz
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.desktop
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.service
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.rsyslog
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.logrotate
# wget https://raw.github.com/RussianFedora/minetest/fedora/minetest.README

Source0:	%name-%version.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.service
Source3:	%{name}.rsyslog
Source4:	%{name}.logrotate
Source5:	%{name}.README
Source6:	%{name}_game-%version.tar.gz
Source7:	http://www.gnu.org/licenses/lgpl-2.1.txt

# Fix to build with gcc-4.7.0
Patch1:		%name-0.4.3-gcc.patch

BuildRequires:	cmake >= 2.6.0
BuildRequires:	gcc-c++
BuildRequires:	libirrlicht-devel
BuildRequires:	bzip2-devel jthread-devel libsqlite3-devel
BuildRequires:	libpng-devel libjpeg-devel libXxf86vm-devel libGL-devel
BuildRequires:	libopenal-devel libvorbis-devel
BuildRequires:	systemd

Requires:	%name-server = %version-%release
Requires:	icon-theme-hicolor

%description 
Game of mining, crafting and building in the infinite world of cubic
blocks with optional hostile creatures, features both single and the
network multiplayer mode. There are no in-game sounds yet

%package	server
Summary:	Minetest multiplayer server
Group:		Games/Other

Requires(pre):		shadow-utils

%description	server
Minetest multiplayer server. This package does not require X Window
System.

%prep
%setup -q -n %gitname-%name
%patch1 -p1

pushd games
tar xf %SOURCE6
mv %gitname-%{name}_game %{name}_game
popd

cp %SOURCE7 doc/

%build
%cmake_insource -DJTHREAD_INCLUDE_DIR=%_builddir/%gitname-%name/src/jthread
#pushd BUILD
%make_build
#popd

%install
%makeinstall_std 

# Add desktop file
install -D -m 0644 %SOURCE1 %buildroot%_desktopdir/%name.desktop

# Systemd unit file
mkdir -p %buildroot%_unitdir
cp -p %SOURCE2 %buildroot%_unitdir

# /etc/rsyslog.d/minetest.conf
mkdir -p %buildroot%_sysconfdir/rsyslog.d
cp -p %SOURCE3 %buildroot%_sysconfdir/rsyslog.d/%{name}.conf

# /etc/logrotate.d/minetest
mkdir -p %buildroot/%{_sysconfdir}/logrotate.d
cp -p %SOURCE4 %buildroot/%{_sysconfdir}/logrotate.d/%{name}-server

# /var/lib/minetest directory for server data files
mkdir -p %buildroot%{_sharedstatedir}/%{name} 

# /etc/minetest.conf
mkdir -p %buildroot%{_sysconfdir}
cp -p minetest.conf.example %buildroot%{_sysconfdir}/%{name}.conf

cp -p %SOURCE5 README

# Move doc directory back to the sources
#mkdir __doc
#mv  %buildroot%{_datadir}/doc/%{name}/* __doc
#rm -rf %buildroot%{_datadir}/doc/%{name}

# %find_lang %{name}

%pre server
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d /var/lib/%{name} -s /sbin/nologin \
    -c "Minetest multiplayer server" %{name}
exit 0

%post server
if [ $1 -eq 1 ] ; then 
    # Initial installation 
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%preun server
if [ $1 -eq 0 ] ; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable %{name}.service > /dev/null 2>&1 || :
    /bin/systemctl stop %{name}.service > /dev/null 2>&1 || :
fi

%postun server
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart %{name}.service >/dev/null 2>&1 || :
fi

# %%files -f %{name}.lang
%files
%doc doc/lgpl-2.1.txt README
%doc %_docdir/%name
%_bindir/%name
%_datadir/%name
%_desktopdir/%{name}.desktop
%_datadir/icons/hicolor/scalable/apps/%{name}-icon.svg
%_man6dir/minetest.*

%files server
%doc README.txt doc/lgpl-2.1.txt doc/mapformat.txt doc/protocol.txt README
%_bindir/%{name}server
%_unitdir/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}-server
%config(noreplace) %{_sysconfdir}/rsyslog.d/%{name}.conf
%attr(0755,minetest,minetest) %dir %{_sharedstatedir}/%{name}
%_man6dir/minetestserver.*


%changelog
* Mon Jul 29 2013 Andrey Cherepanov <cas@altlinux.org> 0.4.7-alt1
- Initial build in Sisyphus (thanks Fedora maintainers)

