# BEGIN SourceDeps(oneline):
BuildRequires: /usr/bin/desktop-file-install /usr/bin/glib-gettextize
# END SourceDeps(oneline)
%define fedora 25
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:		gtorrentviewer
Version:	0.2b
Release:	alt4_36
Summary:	A GTK2-based viewer and editor for BitTorrent meta files
Group:		Networking/WWW
License:	GPL+
URL:		http://gtorrentviewer.sourceforge.net/
Source0:	http://downloads.sf.net/gtorrentviewer/GTorrentViewer-%{version}.tar.gz
Patch0:		gtorrentviewer-0.2b-desktop.patch
Patch1:		gtorrentviewer-0.2b-dso-linking.patch
Patch2:		GTorrentViewer-0.2b-tracker-details-refresh.patch
Patch3:		gtorrentviewer-0.2b-trackerdetails.patch
Patch4:		GTorrentViewer-0.2b-curl-types.patch
Patch5:		GTorrentViewer-0.2b-format.patch
Patch6:		GTorrentViewer-0.2b-missing-tracker.patch
BuildRequires:	libcurl-devel gtk-builder-convert gtk-demo libgail-devel libgtk+2-devel libgtk+2-gir-devel, desktop-file-utils gettext gettext-tools, intltool

Requires(post):	  desktop-file-utils
Requires(postun): desktop-file-utils
Source44: import.info

%description
GTorrentViewer gives you the ability to see and modify all the possible
information from .torrent files without having to start downloading, and
the ability to see in real time the current number of seeds and peers on
the torrent, so you will always know the status before starting the
download.

%prep
%setup -q -n GTorrentViewer-%{version}

# Let drag and drop work with URIs as well as files (#206262)
# Also drop ".png" suffix from icon filename, as per Icon Theme spec
%patch0

# mainwindow.c requires ceil() from libm (#564928)
%patch1 -p1

# Fix crash due to use of uninitialized GValue (#542502, #572806)
%patch2 -p1

# Improve tracker support (#674726)
%patch3 -p1

# <curl/types.h> went away in curl 7.22.0
%patch4 -p1

# Add missing format strings in g_warning() invocations
%patch5

# Avoid segfault when dealing with torrent that has no tracker (#1178062)
%patch6

# curl/types.h are no more; was true for  0.2b-22.
sed -i 's,#include <curl/types.h>,,' src/main.c

%build
%configure
%make_build

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"
rm -f %{buildroot}%{_datadir}/GTorrentViewer/README
desktop-file-install \
%if 0%{?fedora} < 19 && 0%{?rhel} < 4
	--vendor fedora \
%else
	--vendor "" \
%endif
	--add-category X-Fedora \
	--delete-original \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/gtorrentviewer.desktop

desktop-file-install --dir %buildroot%_desktopdir \
        --add-category=FileTransfer \
        --add-category=P2P \
        %buildroot%_desktopdir/gtorrentviewer.desktop

%files
%if 0%{?_licensedir:1}
%doc COPYING
%else
%doc COPYING
%endif
%doc AUTHORS ChangeLog README
%{_bindir}/gtorrentviewer
%{_datadir}/GTorrentViewer
%if 0%{?fedora} < 19 && 0%{?rhel} < 4
%{_datadir}/applications/fedora-gtorrentviewer.desktop
%else
%{_datadir}/applications/gtorrentviewer.desktop
%endif
%{_datadir}/pixmaps/gtorrentviewer.png
%{_datadir}/pixmaps/gtorrentviewer.xpm
%{_mandir}/man1/gtorrentviewer.1*

%changelog
* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_36
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_34
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_33
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_32
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_31
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_30
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_29
- update to new release by fcimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_28
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_27
- fc update

* Fri Feb 15 2013 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_26
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_25
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt4_24
- rebuild to get rid of #27020

* Wed Jan 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt3_24
- update to new release by fcimport

* Mon Nov 07 2011 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt3_23
- update to new release by fcimport

* Tue Jul 05 2011 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt3_22
- fixed build

* Tue Jun 07 2011 Repocop Q. A. Robot <repocop@altlinux.org> 0.2b-alt2_22.qa1
- NMU (by repocop). See http://www.altlinux.org/Tools/Repocop
- applied repocop fixes:
  * freedesktop-desktop-file-proposed-patch for gtorrentviewer
  * postclean-03-private-rpm-macros for the spec file

* Wed May 25 2011 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt2_22
- fixed scripts

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.2b-alt1_22
- initial release by fcimport

