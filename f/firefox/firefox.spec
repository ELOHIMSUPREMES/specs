#set_verify_elf_method relaxed

%define firefox_cid                    \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%define firefox_prefix                 %_libdir/firefox
%define firefox_datadir                %_datadir/firefox

Summary:              The Mozilla Firefox project is a redesign of Mozilla's browser
Summary(ru_RU.UTF-8): Интернет-браузер Mozilla Firefox

Name:           firefox
Version:        26.0
Release:        alt1
License:        MPL/GPL/LGPL
Group:          Networking/WWW
URL:            http://www.mozilla.org/projects/firefox/

Packager:	Alexey Gladkov <legion@altlinux.ru>

Source0:	firefox-source.tar
Source1:	rpm-build.tar
Source2:	searchplugins.tar
Source4:	firefox-mozconfig
Source6:	firefox.desktop
Source7:	firefox.c
Source8:	firefox-prefs.js

Patch6:		firefox3-alt-disable-werror.patch
Patch14:	firefox-fix-install.patch
Patch16:	firefox-cross-desktop.patch
#Patch17:	firefox-disable-installer.patch
Patch20:	mozilla-938730.patch

BuildRequires(pre): mozilla-common-devel
BuildRequires(pre): rpm-build-mozilla.org
BuildRequires(pre): browser-plugins-npapi-devel

BuildRequires: doxygen gcc-c++ imake libIDL-devel makedepend
BuildRequires: libXt-devel libX11-devel libXext-devel libXft-devel libXScrnSaver-devel
BuildRequires: libcurl-devel libgtk+2-devel libhunspell-devel libjpeg-devel
BuildRequires: xorg-cf-files chrpath alternatives yasm
BuildRequires: bzlib-devel zlib-devel
BuildRequires: libcairo-devel libpixman-devel
BuildRequires: libGL-devel
BuildRequires: libwireless-devel
BuildRequires: libalsa-devel
BuildRequires: libnotify-devel
BuildRequires: libevent-devel
BuildRequires: zip unzip
BuildRequires: libshell
BuildRequires: libvpx-devel
BuildRequires: libgio-devel
BuildRequires: libfreetype-devel fontconfig-devel
BuildRequires: libstartup-notification-devel
BuildRequires: rpm-macros-alternatives
BuildRequires: gstreamer-devel gst-plugins-devel

# Python requires
BuildRequires: python-module-distribute
BuildRequires: python-modules-compiler
BuildRequires: python-modules-logging
BuildRequires: python-modules-sqlite3
BuildRequires: python-modules-json

# Mozilla requires
BuildRequires: xulrunner-devel     >= 20.0-alt1
BuildRequires: libnspr-devel       >= 4.9.6-alt1
BuildRequires: libnss-devel        >= 3.14.3-alt1
BuildRequires: libnss-devel-static >= 3.14.3-alt1

BuildRequires: autoconf_2.13
%set_autoconf_version 2.13

Obsoletes:	firefox-3.6 firefox-4.0 firefox-5.0
Conflicts:	firefox-settings-desktop

Provides:	webclient
Requires:	mozilla-common

# Protection against fraudulent DigiNotar certificates
Requires: libnss >= 3.12.11-alt3

%description
The Mozilla Firefox project is a redesign of Mozilla's browser component,
written using the XUL user interface language and designed to be
cross-platform.

%description -l ru_RU.UTF8
Интернет-браузер Mozilla Firefox - кроссплатформенная модификация браузера Mozilla,
созданная с использованием языка XUL для описания интерфейса пользователя.

%package -n rpm-build-firefox
Summary:	RPM helper macros to rebuild firefox packages
Group:		Development/Other
BuildArch:	noarch

Requires:	mozilla-common-devel
Requires:	rpm-build-mozilla.org

%description -n rpm-build-firefox
These helper macros provide possibility to rebuild
firefox packages by some Alt Linux Team Policy compatible way.

%prep
%setup -q -n firefox-%version -c
cd mozilla

tar -xf %SOURCE1
tar -xf %SOURCE2

%patch6  -p1
%patch14 -p1
%patch16 -p1
#patch17 -p1
%patch20 -p1 -b .938730

#echo firefox_version > browser/config/version.txt

cp -f %SOURCE4 .mozconfig

%build
cd mozilla

%add_optflags %optflags_shared

export MOZ_BUILD_APP=browser

cat >> browser/confvars.sh <<EOF
MOZ_UPDATER=
MOZ_EXTENSIONS_DEFAULT=' gio'
MOZ_CHROME_FILE_FORMAT=jar
EOF

# Mozilla builds with -Wall with exception of a few warnings which show up
# everywhere in the code; so, don't override that.
#
# Disable C++ exceptions since Mozilla code is not exception-safe
#
MOZ_OPT_FLAGS=$(echo $RPM_OPT_FLAGS | \
                sed -e 's/-Wall//' -e 's/-fexceptions/-fno-exceptions/g')
export CFLAGS="$MOZ_OPT_FLAGS"
export CXXFLAGS="$MOZ_OPT_FLAGS"
export LDFLAGS='-Wl,-rpath-link,%xulr_develdir/lib'

export PREFIX="%_prefix"
export LIBDIR="%_libdir"
export XULSDK="%xulr_develdir"
export LIBIDL_CONFIG=/usr/bin/libIDL-config-2
export srcdir="$PWD"
export SHELL=/bin/sh

%__autoconf

# On x86 architectures, Mozilla can build up to 4 jobs at once in parallel,
# however builds tend to fail on other arches when building in parallel.
MOZ_SMP_FLAGS=-j1
%ifarch %{ix86} x86_64
[ "${NPROCS:+0}" -ge 2 ] && MOZ_SMP_FLAGS=-j2
[ "${NPROCS:+0}" -ge 4 ] && MOZ_SMP_FLAGS=-j4
%endif

make -f client.mk \
	MAKENSISU= \
	STRIP="/bin/true" \
	MOZ_MAKE_FLAGS="$MOZ_SMP_FLAGS" \
	mozappdir=%buildroot/%firefox_prefix \
	build

%__cc %optflags \
	-Wall -Wextra \
	-DMOZ_PLUGIN_PATH=\"%browser_plugins_path\" \
	-DXUL_APP_FILE=\"%firefox_prefix/browser/application.ini\" \
	%SOURCE7 -o firefox


%install
cd mozilla

%__mkdir_p \
	%buildroot/%mozilla_arch_extdir/%firefox_cid \
	%buildroot/%mozilla_noarch_extdir/%firefox_cid \
	#

make -C objdir \
    DESTDIR=%buildroot \
    INSTALL="/bin/install -p" \
    mozappdir=%firefox_prefix \
    install

# install altlinux-specific configuration
install -D -m 644 %SOURCE8 %buildroot/%firefox_prefix/browser/defaults/preferences/all-altlinux.js

cat > %buildroot/%firefox_prefix/browser/defaults/preferences/firefox-l10n.js <<EOF
pref("intl.locale.matchOS",		true);
pref("general.useragent.locale",	"chrome://global/locale/intl.properties");
EOF

# icons
for s in 16 22 24 32 48 256; do
	install -D -m 644 \
		browser/branding/official/default$s.png \
		%buildroot/%_iconsdir/hicolor/${s}x${s}/apps/firefox.png
done

# searchplugins
cp -a -- \
	searchplugins/* \
	%buildroot/%firefox_prefix/browser/searchplugins/

# install rpm-build-firefox
mkdir -p -- \
	%buildroot/%_rpmmacrosdir
sed \
	-e 's,@firefox_version@,%version,' \
	-e 's,@firefox_release@,%release,' \
	rpm-build/rpm.macros.firefox.standalone > %buildroot/%_rpmmacrosdir/firefox

install -m755 firefox %buildroot/%_bindir/firefox

cd %buildroot

#sed -i \
#	-e 's,\(MinVersion\)=.*,\1=5.0.1,g' \
#	-e 's,\(MaxVersion\)=.*,\1=5.0.1,g' \
#	./%firefox_prefix/application.ini

mv -f ./%firefox_prefix/application.ini ./%firefox_prefix/browser/application.ini

# install menu file
%__install -D -m 644 %SOURCE6 ./%_datadir/applications/firefox.desktop

# Add alternatives
mkdir -p ./%_altdir
printf '%_bindir/xbrowser\t%_bindir/firefox\t100\n' >./%_altdir/firefox

rm -f -- \
	./%firefox_prefix/firefox \
	./%firefox_prefix/removed-files

%pre
for n in defaults browserconfig.properties; do
	[ ! -L "%firefox_prefix/$n" ] || rm -f "%firefox_prefix/$n"
done

%files
%_altdir/firefox
%_bindir/firefox
%firefox_prefix
%mozilla_arch_extdir/%firefox_cid
%mozilla_noarch_extdir/%firefox_cid
%_datadir/applications/firefox.desktop
%_iconsdir/hicolor/16x16/apps/firefox.png
%_iconsdir/hicolor/22x22/apps/firefox.png
%_iconsdir/hicolor/24x24/apps/firefox.png
%_iconsdir/hicolor/32x32/apps/firefox.png
%_iconsdir/hicolor/48x48/apps/firefox.png
%_iconsdir/hicolor/256x256/apps/firefox.png

%files -n rpm-build-firefox
%_rpmmacrosdir/firefox

%changelog
* Mon Dec 23 2013 Alexey Gladkov <legion@altlinux.ru> 26.0-alt1
- New release (26.0).
- Fixed:
  + MFSA 2013-117 Mis-issued ANSSI/DCSSI certificate
  + MFSA 2013-116 JPEG information leak
  + MFSA 2013-115 GetElementIC typed array stubs can be generated outside observed typesets
  + MFSA 2013-114 Use-after-free in synthetic mouse movement
  + MFSA 2013-113 Trust settings for built-in roots ignored during EV certificate validation
  + MFSA 2013-112 Linux clipboard information disclosure though selection paste
  + MFSA 2013-111 Segmentation violation when replacing ordered list elements
  + MFSA 2013-110 Potential overflow in JavaScript binary search algorithms
  + MFSA 2013-109 Use-after-free during Table Editing
  + MFSA 2013-108 Use-after-free in event listeners
  + MFSA 2013-107 Sandbox restrictions not applied to nested object elements
  + MFSA 2013-106 Character encoding cross-origin XSS attack
  + MFSA 2013-105 Application Installation doorhanger persists on navigation
  + MFSA 2013-104 Miscellaneous memory safety hazards (rv:26.0 / rv:24.2)

* Thu Nov 21 2013 Alexey Gladkov <legion@altlinux.ru> 25.0.1-alt1
- New release (25.0.1).
- Fixed:
  + MFSA 2013-103 Miscellaneous Network Security Services (NSS) vulnerabilities

* Sun Nov 03 2013 Alexey Gladkov <legion@altlinux.ru> 25.0-alt1
- New release (25.0).
- Fixed:
  + MFSA 2013-102 Use-after-free in HTML document templates
  + MFSA 2013-101 Memory corruption in workers
  + MFSA 2013-100 Miscellaneous use-after-free issues found through ASAN fuzzing
  + MFSA 2013-99 Security bypass of PDF.js checks using iframes
  + MFSA 2013-98 Use-after-free when updating offline cache
  + MFSA 2013-97 Writing to cycle collected object during image decoding
  + MFSA 2013-96 Improperly initialized memory and overflows in some JavaScript functions
  + MFSA 2013-95 Access violation with XSLT and uninitialized data
  + MFSA 2013-94 Spoofing addressbar though SELECT element
  + MFSA 2013-93 Miscellaneous memory safety hazards (rv:25.0 / rv:24.1 / rv:17.0.10)

* Tue Oct 01 2013 Alexey Gladkov <legion@altlinux.ru> 24.0-alt1
- New release (24.0).
- Add gstreamer support (ALT#29454).
- Fixed:
  + MFSA 2013-92 GC hazard with default compartments and frame chain restoration
  + MFSA 2013-91 User-defined properties on DOM proxies get the wrong "this" object
  + MFSA 2013-90 Memory corruption involving scrolling
  + MFSA 2013-89 Buffer overflow with multi-column, lists, and floats
  + MFSA 2013-88 compartment mismatch re-attaching XBL-backed nodes
  + MFSA 2013-87 Shared object library loading from writable location
  + MFSA 2013-86 WebGL Information disclosure through OS X NVIDIA graphic drivers
  + MFSA 2013-85 Uninitialized data in IonMonkey
  + MFSA 2013-84 Same-origin bypass through symbolic links
  + MFSA 2013-83 Mozilla Updater does not lock MAR file after signature verification
  + MFSA 2013-82 Calling scope for new Javascript objects can lead to memory corruption
  + MFSA 2013-81 Use-after-free with select element
  + MFSA 2013-80 NativeKey continues handling key messages after widget is destroyed
  + MFSA 2013-79 Use-after-free in Animation Manager during stylesheet cloning
  + MFSA 2013-78 Integer overflow in ANGLE library
  + MFSA 2013-77 Improper state in HTML5 Tree Builder with templates
  + MFSA 2013-76 Miscellaneous memory safety hazards (rv:24.0 / rv:17.0.9)

* Mon Aug 12 2013 Alexey Gladkov <legion@altlinux.ru> 23.0-alt1
- New release (23.0).
- Fixed:
  + MFSA 2013-75 Local Java applets may read contents of local file system
  + MFSA 2013-74 Firefox full and stub installer DLL hijacking
  + MFSA 2013-73 Same-origin bypass with web workers and XMLHttpRequest
  + MFSA 2013-72 Wrong principal used for validating URI for some Javascript components
  + MFSA 2013-71 Further Privilege escalation through Mozilla Updater
  + MFSA 2013-70 Bypass of XrayWrappers using XBL Scopes
  + MFSA 2013-69 CRMF requests allow for code execution and XSS attacks
  + MFSA 2013-68 Document URI misrepresentation and masquerading
  + MFSA 2013-67 Crash during WAV audio file decoding
  + MFSA 2013-66 Buffer overflow in Mozilla Maintenance Service and Mozilla Updater
  + MFSA 2013-65 Buffer underflow when generating CRMF requests
  + MFSA 2013-64 Use after free mutating DOM during SetBody
  + MFSA 2013-63 Miscellaneous memory safety hazards (rv:23.0 / rv:17.0.8)

* Wed Jun 26 2013 Alexey Gladkov <legion@altlinux.ru> 22.0-alt1
- New release (22.0).
- Fixed:
  + MFSA 2013-62 Inaccessible updater can lead to local privilege escalation
  + MFSA 2013-61 Homograph domain spoofing in .com, .net and .name
  + MFSA 2013-60 getUserMedia permission dialog incorrectly displays location
  + MFSA 2013-59 XrayWrappers can be bypassed to run user defined methods in a privileged context
  + MFSA 2013-58 X-Frame-Options ignored when using server push with multi-part responses
  + MFSA 2013-57 Sandbox restrictions not applied to nested frame elements
  + MFSA 2013-56 PreserveWrapper has inconsistent behavior
  + MFSA 2013-55 SVG filters can lead to information disclosure
  + MFSA 2013-54 Data in the body of XHR HEAD requests leads to CSRF attacks
  + MFSA 2013-53 Execution of unmapped memory through onreadystatechange event
  + MFSA 2013-52 Arbitrary code execution within Profiler
  + MFSA 2013-51 Privileged content access and execution via XBL
  + MFSA 2013-50 Memory corruption found using Address Sanitizer
  + MFSA 2013-49 Miscellaneous memory safety hazards (rv:22.0 / rv:17.0.7)

* Sat Jun 01 2013 Alexey Gladkov <legion@altlinux.ru> 21.0-alt1
- New release (21.0).
- Fixed:
  + MFSA 2013-48 Memory corruption found using Address Sanitizer
  + MFSA 2013-47 Uninitialized functions in DOMSVGZoomEvent
  + MFSA 2013-46 Use-after-free with video and onresize event
  + MFSA 2013-45 Mozilla Updater fails to update some Windows Registry entries
  + MFSA 2013-44 Local privilege escalation through Mozilla Maintenance Service
  + MFSA 2013-43 File input control has access to full path
  + MFSA 2013-42 Privileged access for content level constructor
  + MFSA 2013-41 Miscellaneous memory safety hazards (rv:21.0 / rv:17.0.6)

* Wed Apr 10 2013 Alexey Gladkov <legion@altlinux.ru> 20.0-alt1
- New release (20.0).
- Fixed:
  + MFSA 2013-40 Out-of-bounds array read in CERT_DecodeCertPackage
  + MFSA 2013-39 Memory corruption while rendering grayscale PNG images
  + MFSA 2013-38 Cross-site scripting (XSS) using timed history navigations
  + MFSA 2013-37 Bypass of tab-modal dialog origin disclosure
  + MFSA 2013-36 Bypass of SOW protections allows cloning of protected nodes
  + MFSA 2013-35 WebGL crash with Mesa graphics driver on Linux
  + MFSA 2013-34 Privilege escalation through Mozilla Updater
  + MFSA 2013-33 World read and write access to app_tmp directory on Android
  + MFSA 2013-32 Privilege escalation through Mozilla Maintenance Service
  + MFSA 2013-31 Out-of-bounds write in Cairo library
  + MFSA 2013-30 Miscellaneous memory safety hazards (rv:20.0 / rv:17.0.5)

* Sat Mar 09 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.2-alt1
- New release (19.0.2).
- Fixed:
  + MFSA 2013-29 Use-after-free in HTML Editor

* Fri Mar 01 2013 Alexey Gladkov <legion@altlinux.ru> 19.0.1-alt1
- New release (19.0.1).
- Fixed:
  + MFSA 2013-28 Use-after-free, out of bounds read, and buffer overflow issues found using Address Sanitizer
  + MFSA 2013-27 Phishing on HTTPS connection through malicious proxy
  + MFSA 2013-26 Use-after-free in nsImageLoadingContent
  + MFSA 2013-25 Privacy leak in JavaScript Workers
  + MFSA 2013-24 Web content bypass of COW and SOW security wrappers
  + MFSA 2013-23 Wrapped WebIDL objects can be wrapped again
  + MFSA 2013-22 Out-of-bounds read in image rendering
  + MFSA 2013-21 Miscellaneous memory safety hazards (rv:19.0 / rv:17.0.3)

* Sun Feb 10 2013 Alexey Gladkov <legion@altlinux.ru> 18.0.2-alt1
- New release (18.0.2).

* Mon Jan 28 2013 Alexey Gladkov <legion@altlinux.ru> 18.0.1-alt1
- New release (18.0.1).

* Thu Jan 17 2013 Alexey Gladkov <legion@altlinux.ru> 18.0-alt1
- New release (18.0).
- Fixed:
  + MFSA 2013-20 Mis-issued TURKTRUST certificates
  + MFSA 2013-19 Use-after-free in Javascript Proxy objects
  + MFSA 2013-18 Use-after-free in Vibrate
  + MFSA 2013-17 Use-after-free in ListenerManager
  + MFSA 2013-16 Use-after-free in serializeToStream
  + MFSA 2013-15 Privilege escalation through plugin objects
  + MFSA 2013-14 Chrome Object Wrapper (COW) bypass through changing prototype
  + MFSA 2013-13 Memory corruption in XBL with XML bindings containing SVG
  + MFSA 2013-12 Buffer overflow in Javascript string concatenation
  + MFSA 2013-11 Address space layout leaked in XBL objects
  + MFSA 2013-10 Event manipulation in plugin handler to bypass same-origin policy
  + MFSA 2013-09 Compartment mismatch with quickstubs returned values
  + MFSA 2013-08 AutoWrapperChanger fails to keep objects alive during garbage collection
  + MFSA 2013-07 Crash due to handling of SSL on threads
  + MFSA 2013-06 Touch events are shared across iframes
  + MFSA 2013-05 Use-after-free when displaying table with many columns and column groups
  + MFSA 2013-04 URL spoofing in addressbar during page loads
  + MFSA 2013-03 Buffer Overflow in Canvas
  + MFSA 2013-02 Use-after-free and buffer overflow issues found using Address Sanitizer
  + MFSA 2013-01 Miscellaneous memory safety hazards (rv:18.0/ rv:10.0.12 / rv:17.0.2)
  + MFSA 2012-98 Firefox installer DLL hijacking

* Wed Dec 05 2012 Alexey Gladkov <legion@altlinux.ru> 17.0.1-alt1
- New release (17.0.1).

* Wed Nov 21 2012 Alexey Gladkov <legion@altlinux.ru> 17.0-alt1
- New release (17.0).
- Fixed:
  + MFSA 2012-106 Use-after-free, buffer overflow, and memory corruption issues found using Address Sanitizer
  + MFSA 2012-105 Use-after-free and buffer overflow issues found using Address Sanitizer
  + MFSA 2012-104 CSS and HTML injection through Style Inspector
  + MFSA 2012-103 Frames can shadow top.location
  + MFSA 2012-102 Script entered into Developer Toolbar runs with chrome privileges
  + MFSA 2012-101 Improper character decoding in HZ-GB-2312 charset
  + MFSA 2012-100 Improper security filtering for cross-origin wrappers
  + MFSA 2012-99 XrayWrappers exposes chrome-only properties when not in chrome compartment
  + MFSA 2012-98 Firefox installer DLL hijacking
  + MFSA 2012-97 XMLHttpRequest inherits incorrect principal within sandbox
  + MFSA 2012-96 Memory corruption in str_unescape
  + MFSA 2012-95 Javascript: URLs run in privileged context on New Tab page
  + MFSA 2012-94 Crash when combining SVG text on path with CSS
  + MFSA 2012-93 evalInSanbox location context incorrectly applied
  + MFSA 2012-92 Buffer overflow while rendering GIF images
  + MFSA 2012-91 Miscellaneous memory safety hazards (rv:17.0/ rv:10.0.11)

* Thu Nov 01 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.2-alt1
- New release (16.0.2).
- Fixed:
  + MFSA 2012-90 Fixes for Location object issues

* Mon Oct 22 2012 Alexey Gladkov <legion@altlinux.ru> 16.0.1-alt1
- New release (16.0.1).
- Fixed:
  + MFSA 2012-89 defaultValue security checks not applied
  + MFSA 2012-88 Miscellaneous memory safety hazards (rv:16.0.1)
  + MFSA 2012-87 Use-after-free in the IME State Manager
  + MFSA 2012-86 Heap memory corruption issues found using Address Sanitizer
  + MFSA 2012-85 Use-after-free, buffer overflow, and out of bounds read issues found using Address Sanitizer
  + MFSA 2012-84 Spoofing and script injection through location.hash
  + MFSA 2012-83 Chrome Object Wrapper (COW) does not disallow acces to privileged functions or properties
  + MFSA 2012-82 top object and location property accessible by plugins
  + MFSA 2012-81 GetProperty function can bypass security checks
  + MFSA 2012-80 Crash with invalid cast when using instanceof operator
  + MFSA 2012-79 DOS and crash with full screen and history navigation
  + MFSA 2012-78 Reader Mode pages have chrome privileges
  + MFSA 2012-77 Some DOMWindowUtils methods bypass security checks
  + MFSA 2012-76 Continued access to initial origin after setting document.domain
  + MFSA 2012-75 select element persistance allows for attacks
  + MFSA 2012-74 Miscellaneous memory safety hazards (rv:16.0/ rv:10.0.8)

* Wed Aug 29 2012 Alexey Gladkov <legion@altlinux.ru> 15.0-alt1
- New release (15.0).
- Fixed:
  + MFSA 2012-72 Web console eval capable of executing chrome-privileged code
  + MFSA 2012-71 Insecure use of __android_log_print
  + MFSA 2012-70 Location object security checks bypassed by chrome code
  + MFSA 2012-69 Incorrect site SSL certificate data display
  + MFSA 2012-68 DOMParser loads linked resources in extensions when parsing text/html
  + MFSA 2012-67 Installer will launch incorrect executable following new installation
  + MFSA 2012-66 HTTPMonitor extension allows for remote debugging without explicit activation
  + MFSA 2012-65 Out-of-bounds read in format-number in XSLT
  + MFSA 2012-64 Graphite 2 memory corruption
  + MFSA 2012-63 SVG buffer overflow and use-after-free issues
  + MFSA 2012-62 WebGL use-after-free and memory corruption
  + MFSA 2012-61 Memory corruption with bitmap format images with negative height
  + MFSA 2012-60 Escalation of privilege through about:newtab
  + MFSA 2012-59 Location object can be shadowed using Object.defineProperty
  + MFSA 2012-58 Use-after-free issues found using Address Sanitizer
  + MFSA 2012-57 Miscellaneous memory safety hazards (rv:15.0/ rv:10.0.7)

* Sun Jul 29 2012 Alexey Gladkov <legion@altlinux.ru> 14.0.1-alt1
- New release (14.0.1).
- Fixed:
  + MFSA 2012-56 Code execution through javascript: URLs
  + MFSA 2012-55 feed: URLs with an innerURI inherit security context of page
  + MFSA 2012-53 Content Security Policy 1.0 implementation errors cause data leakage
  + MFSA 2012-52 JSDependentString::undepend string conversion results in memory corruption
  + MFSA 2012-51 X-Frame-Options header ignored when duplicated
  + MFSA 2012-50 Out of bounds read in QCMS
  + MFSA 2012-49 Same-compartment Security Wrappers can be bypassed
  + MFSA 2012-48 use-after-free in nsGlobalWindow::PageHidden
  + MFSA 2012-47 Improper filtering of javascript in HTML feed-view
  + MFSA 2012-46 XSS through data: URLs
  + MFSA 2012-45 Spoofing issue with location
  + MFSA 2012-44 Gecko memory corruption
  + MFSA 2012-43 Incorrect URL displayed in addressbar through drag and drop
  + MFSA 2012-42 Miscellaneous memory safety hazards (rv:14.0/ rv:10.0.6)

* Sun Jul 01 2012 Alexey Gladkov <legion@altlinux.ru> 13.0.1-alt1
- New release (13.0.1).
- Fixed:
  + MFSA 2012-40 Buffer overflow and use-after-free issues found using Address Sanitizer
  + MFSA 2012-39 NSS parsing errors with zero length items
  + MFSA 2012-38 Use-after-free while replacing/inserting a node in a document
  + MFSA 2012-37 Information disclosure though Windows file shares and shortcut files
  + MFSA 2012-36 Content Security Policy inline-script bypass
  + MFSA 2012-35 Privilege escalation through Mozilla Updater and Windows Updater Service
  + MFSA 2012-34 Miscellaneous memory safety hazards

* Tue May 08 2012 Alexey Gladkov <legion@altlinux.ru> 12.0-alt1
- New release (12.0).
- Fixed:
  + MFSA 2012-33 Potential site identity spoofing when loading RSS and Atom feeds
  + MFSA 2012-32 HTTP Redirections and remote content can be read by javascript errors
  + MFSA 2012-31 Off-by-one error in OpenType Sanitizer
  + MFSA 2012-30 Crash with WebGL content using textImage2D
  + MFSA 2012-29 Potential XSS through ISO-2022-KR/ISO-2022-CN decoding issues
  + MFSA 2012-28 Ambiguous IPv6 in Origin headers may bypass webserver access restrictions
  + MFSA 2012-27 Page load short-circuit can lead to XSS
  + MFSA 2012-26 WebGL.drawElements may read illegal video memory due to FindMaxUshortElement error
  + MFSA 2012-25 Potential memory corruption during font rendering using cairo-dwrite
  + MFSA 2012-24 Potential XSS via multibyte content processing errors
  + MFSA 2012-23 Invalid frees causes heap corruption in gfxImageSurface
  + MFSA 2012-22 use-after-free in IDBKeyRange
  + MFSA 2012-21 Multiple security flaws fixed in FreeType v2.4.9
  + MFSA 2012-20 Miscellaneous memory safety hazards (rv:12.0/ rv:10.0.4)

* Thu Apr 19 2012 Alexey Gladkov <legion@altlinux.ru> 11.0-alt1
- New release (11.0).
- Fixed:
  + MFSA 2012-19 Miscellaneous memory safety hazards (rv:11.0/ rv:10.0.3 / rv:1.9.2.28)
  + MFSA 2012-18 window.fullScreen writeable by untrusted content
  + MFSA 2012-17 Crash when accessing keyframe cssText after dynamic modification
  + MFSA 2012-16 Escalation of privilege with Javascript: URL as home page
  + MFSA 2012-15 XSS with multiple Content Security Policy headers
  + MFSA 2012-14 SVG issues found with Address Sanitizer
  + MFSA 2012-13 XSS with Drag and Drop and Javascript: URL
  + MFSA 2012-12 Use-after-free in shlwapi.dll

* Tue Feb 21 2012 Alexey Gladkov <legion@altlinux.ru> 10.0.2-alt1
- New release (10.0.2).
- Fixed:
  + MFSA 2012-11 libpng integer overflow
  + MFSA 2012-10 use after free in nsXBLDocumentInfo::ReadPrototypeBindings
  + MFSA 2012-09 Firefox Recovery Key.html is saved with unsafe permission
  + MFSA 2012-08 Crash with malformed embedded XSLT stylesheets
  + MFSA 2012-07 Potential Memory Corruption When Decoding Ogg Vorbis files
  + MFSA 2012-06 Uninitialized memory appended when encoding icon images may cause information disclosure
  + MFSA 2012-05 Frame scripts calling into untrusted objects bypass security checks
  + MFSA 2012-04 Child nodes from nsDOMAttribute still accessible after removal of nodes
  + MFSA 2012-03 <iframe> element exposed across domains via name attribute
  + MFSA 2012-01 Miscellaneous memory safety hazards (rv:10.0/ rv:1.9.2.26)

* Mon Jan 09 2012 Alexey Gladkov <legion@altlinux.ru> 9.0.1-alt1
- New release (9.0.1).
- Check default browser (ALT#26195).
- Change location for noarch extensions (ALT#26702).
- Add translation for summary and description (ALT#22789).
- Fixed:
  + MFSA 2011-58 Crash scaling <video> to extreme sizes
  + MFSA 2011-57 Crash when plugin removes itself on Mac OS X
  + MFSA 2011-56 Key detection without JavaScript via SVG animation
  + MFSA 2011-55 nsSVGValue out-of-bounds access
  + MFSA 2011-54 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-53 Miscellaneous memory safety hazards (rv:9.0)

* Mon Nov 14 2011 Alexey Gladkov <legion@altlinux.ru> 8.0-alt1
- New release (8.0).
- Fixed:
  + MFSA 2011-52 Code execution via NoWaiverWrapper
  + MFSA 2011-51 Cross-origin image theft on Mac with integrated Intel GPU
  + MFSA 2011-50 Cross-origin data theft using canvas and Windows D2D
  + MFSA 2011-49 Memory corruption while profiling using Firebug
  + MFSA 2011-48 Miscellaneous memory safety hazards (rv:8.0)
  + MFSA 2011-47 Potential XSS against sites using Shift-JIS

* Wed Oct 19 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt2
- Drop depends for extensions.

* Thu Oct 06 2011 Alexey Gladkov <legion@altlinux.ru> 7.0.1-alt1
- New release (7.0.1).
- Fixed:
  + MFSA 2011-45 Inferring Keystrokes from motion data
  + MFSA 2011-44 Use after free reading OGG headers
  + MFSA 2011-43 loadSubScript unwraps XPCNativeWrapper scope parameter
  + MFSA 2011-42 Potentially exploitable crash in the YARR regular expression library
  + MFSA 2011-41 Potentially exploitable WebGL crashes
  + MFSA 2011-40 Code installation through holding down Enter
  + MFSA 2011-39 Defense against multiple Location headers due to CRLF Injection
  + MFSA 2011-36 Miscellaneous memory safety hazards (rv:7.0 / rv:1.9.2.23)

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.2-alt1
- New release (6.0.2).

* Tue Sep 06 2011 Alexey Gladkov <legion@altlinux.ru> 6.0.1-alt1
- New release (6.0.1).
- Fixed:
  + MFSA 2011-34 Protection against fraudulent DigiNotar certificates

* Mon Aug 22 2011 Alexey Gladkov <legion@altlinux.ru> 6.0-alt1
- New release (6.0).
- Add Conflict to firefox-settings-desktop (ALT#25473).
- Fixed:
  + MFSA 2011-29 Security issues addressed in Firefox6.

* Wed Jul 13 2011 Alexey Gladkov <legion@altlinux.ru> 5.0.1-alt1
- New release (5.0.1).
- Fixed:
  + MFSA 2011-28 Non-whitelisted site can trigger xpinstall
  + MFSA 2011-27 XSS encoding hazard with inline SVG
  + MFSA 2011-26 Multiple WebGL crashes
  + MFSA 2011-25 Stealing of cross-domain images using WebGL textures
  + MFSA 2011-22 Integer overflow and arbitrary code execution in Array.reduceRight()
  + MFSA 2011-21 Memory corruption due to multipart/x-mixed-replace images
  + MFSA 2011-20 Use-after-free vulnerability when viewing XUL document with script disabled
  + MFSA 2011-19 Miscellaneous memory safety hazards (rv:3.0/1.9.2.18)

* Mon May 02 2011 Alexey Gladkov <legion@altlinux.ru> 4.0.1-alt1
- New release (4.0.1).
- Update desktop file (ALT#25530).
- Fixed:
  + MFSA 2011-18 XSLT generate-id() function heap address leak
  + MFSA 2011-17 WebGLES vulnerabilities
  + MFSA 2011-12 Miscellaneous memory safety hazards (rv:2.0.1/ 1.9.2.17/ 1.9.1.19)

* Fri Apr 22 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt3
- Set some settings in Firefox to default values (ALT#22148).

* Tue Apr 19 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt2
- Fix plugins path.
- Fix alternatives for %_bindir/xbrowser.

* Fri Apr 01 2011 Alexey Gladkov <legion@altlinux.ru> 4.0-alt1
- New release (4.0).
- Remove alternatives for configuration.

* Tue Mar 08 2011 Alexey Gladkov <legion@altlinux.ru> 3.6.15-alt1.20110308
- New release (3.6.15).
- Fixed:
  + MFSA 2011-10 CSRF risk with plugins and 307 redirects
  + MFSA 2011-09 Crash caused by corrupted JPEG image
  + MFSA 2011-08 ParanoidFragmentSink allows javascript: URLs in chrome documents
  + MFSA 2011-07 Memory corruption during text run construction (Windows)
  + MFSA 2011-06 Use-after-free error using Web Workers
  + MFSA 2011-05 Buffer overflow in JavaScript atom map
  + MFSA 2011-04 Buffer overflow in JavaScript upvarMap
  + MFSA 2011-03 Use-after-free error in JSON.stringify
  + MFSA 2011-02 Recursive eval call causes confirm dialogs to evaluate to true
  + MFSA 2011-01 Miscellaneous memory safety hazards (rv:1.9.2.14/ 1.9.1.17)

* Wed Dec 22 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.13-alt1.20101222
- New release (3.6.13).
- Fixed:
  + MFSA 2010-84 XSS hazard in multiple character encodings
  + MFSA 2010-83 Location bar SSL spoofing using network error page
  + MFSA 2010-82 Incomplete fix for CVE-2010-0179
  + MFSA 2010-81 Integer overflow vulnerability in NewIdArray
  + MFSA 2010-80 Use-after-free error with nsDOMAttribute MutationObserver
  + MFSA 2010-79 Java security bypass from LiveConnect loaded via data: URL meta refresh
  + MFSA 2010-78 Add support for OTS font sanitizer
  + MFSA 2010-77 Crash and remote code execution using HTML tags inside a XUL tree
  + MFSA 2010-76 Chrome privilege escalation with window.open and <isindex> element
  + MFSA 2010-75 Buffer overflow while line breaking after document.write with long string
  + MFSA 2010-74 Miscellaneous memory safety hazards (rv:1.9.2.13/ 1.9.1.16)

* Sun Nov 14 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.13-alt1.20101110
- New release (3.6.12).
- Fixed:
  + MFSA 2010-73 Heap buffer overflow mixing document.write and DOM insertion

* Tue Oct 26 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.12-alt1.20101025
- New release (3.6.11).
- Fixed:
  + MFSA 2010-72 Insecure Diffie-Hellman key exchange
  + MFSA 2010-71 Unsafe library loading vulnerabilities
  + MFSA 2010-70 SSL wildcard certificate matching IP addresses
  + MFSA 2010-69 Cross-site information disclosure via modal calls
  + MFSA 2010-68 XSS in gopher parser when parsing hrefs
  + MFSA 2010-67 Dangling pointer vulnerability in LookupGetterOrSetter
  + MFSA 2010-66 Use-after-free error in nsBarProp
  + MFSA 2010-65 Buffer overflow and memory corruption using document.write
  + MFSA 2010-64 Miscellaneous memory safety hazards (rv:1.9.2.11/ 1.9.1.14)

* Tue Sep 21 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.11-alt1.20100920
- New release (3.6.10).

* Sun Sep 12 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.10-alt1.20100909
- New release (3.6.9).
- Fixed:
  + MFSA 2010-63 Information leak via XMLHttpRequest statusText
  + MFSA 2010-62 Copy-and-paste or drag-and-drop into designMode document allows XSS
  + MFSA 2010-61 UTF-7 XSS by overriding document charset using <object> type attribute
  + MFSA 2010-59 SJOW creates scope chains ending in outer object
  + MFSA 2010-58 Crash on Mac using fuzzed font in data: URL
  + MFSA 2010-57 Crash and remote code execution in normalizeDocument
  + MFSA 2010-56 Dangling pointer vulnerability in nsTreeContentView
  + MFSA 2010-55 XUL tree removal crash and remote code execution
  + MFSA 2010-54 Dangling pointer vulnerability in nsTreeSelection
  + MFSA 2010-53 Heap buffer overflow in nsTextFrameUtils::TransformText
  + MFSA 2010-52 Windows XP DLL loading vulnerability
  + MFSA 2010-51 Dangling pointer vulnerability using DOM plugin array
  + MFSA 2010-50 Frameset integer overflow vulnerability
  + MFSA 2010-49 Miscellaneous memory safety hazards (rv:1.9.2.9/ 1.9.1.12)

* Thu Jul 29 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.9-alt1.20100725
- New release (3.6.8).
- Fixed:
  + MFSA 2010-48 Dangling pointer crash regression from plugin parameter array fix
  + MFSA 2010-47 Cross-origin data leakage from script filename in error messages
  + MFSA 2010-46 Cross-domain data theft using CSS
  + MFSA 2010-45 Multiple location bar spoofing vulnerabilities
  + MFSA 2010-44 Characters mapped to U+FFFD in 8 bit encodings cause subsequent character to vanish
  + MFSA 2010-43 Same-origin bypass using canvas context
  + MFSA 2010-42 Cross-origin data disclosure via Web Workers and importScripts
  + MFSA 2010-41 Remote code execution using malformed PNG image
  + MFSA 2010-40 nsTreeSelection dangling pointer remote code execution vulnerability
  + MFSA 2010-39 nsCSSValue::Array index integer overflow
  + MFSA 2010-38 Arbitrary code execution using SJOW and fast native function
  + MFSA 2010-37 Plugin parameter EnsureCachedAttrParamArrays remote code execution vulnerability
  + MFSA 2010-36 Use-after-free error in NodeIterator
  + MFSA 2010-35 DOM attribute cloning remote code execution vulnerability
  + MFSA 2010-34 Miscellaneous memory safety hazards (rv:1.9.2.7/ 1.9.1.11)

* Sun Jun 27 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.6-alt1.20100626
- New release (3.6.6).
- Fixed:
  + MFSA 2010-33 User tracking across sites using Math.random()
  + MFSA 2010-32 Content-Disposition: attachment ignored if Content-Type: multipart also present
  + MFSA 2010-31 focus() behavior can be used to inject or steal keystrokes
  + MFSA 2010-30 Integer Overflow in XSLT Node Sorting
  + MFSA 2010-29 Heap buffer overflow in nsGenericDOMDataNode::SetTextInternal
  + MFSA 2010-28 Freed object reuse across plugin instances
  + MFSA 2010-26 Crashes with evidence of memory corruption (rv:1.9.2.4/ 1.9.1.10)

* Mon Apr 05 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.3-alt1.20100404
- New release (3.6.3).
- Fixed:
  + MFSA 2009-25 Re-use of freed object due to scope confusion

* Mon Mar 29 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.2-alt1.20100328
- New release (3.6.2).
- Fix for Transport Layer Security (ALT#22994).
- Fix addons search (ALT#22878).
- Fix release notes (ALT#22883).
- Fixed:
  + MFSA 2010-15 Asynchronous Auth Prompt attaches to wrong window
  + MFSA 2010-14 Browser chrome defacement via cached XUL stylesheets
  + MFSA 2010-13 Content policy bypass with image preloading
  + MFSA 2010-12 XSS using addEventListener and setTimeout on a wrapped object
  + MFSA 2010-11 Crashes with evidence of memory corruption (rv:1.9.2.2/ 1.9.1.8/ 1.9.0.18)
  + MFSA 2010-10 XSS via plugins and unprotected Location object
  + MFSA 2010-09 Deleted frame reuse in multipart/x-mixed-replace image
  + MFSA 2010-08 WOFF heap corruption due to integer overflow

* Fri Jan 22 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt1
- New release (3.6.0).
- Fix process name (ALT#22731).

* Thu Jan 07 2010 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt0.20100113
- New snapshot (3.6.0 20100113).

* Mon Nov 24 2009 Alexey Gladkov <legion@altlinux.ru> 3.6.0-alt0.20091124
- New major branch (3.6.0 b4pre).

* Sun Oct 11 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20091010
- New snapshot (3.5.3 20091010).
- KDE: Update patches (ALT#21509).

* Mon Sep 28 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090918.1
- Rebuild with new browser-plugins-npapi.

* Sun Sep 20 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090918
- New snapshot (3.5.3 20090918).
- Set firefox as default KDE/KDE4 browser (ALT#21509).
- Update desktop file (ALT#21510).
- Update requires (ALT#21533).

* Tue Sep 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.3-alt0.20090831
- New snapshot (3.5.3 20090831).

* Fri Jul 17 2009 Alexey Gladkov <legion@altlinux.ru> 3.5.1-alt1
- New release (3.5.1).

* Wed Jul 01 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt2
- New release (3.5).

* Thu Jun 04 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt1.20090601
- New snapshot (3.5 20090601).

* Wed Apr 24 2009 Alexey Gladkov <legion@altlinux.ru> 3.5-alt1.20090424
- New snapshot (3.5 20090424).

* Sun Jan 18 2009 Alexey Gladkov <legion@altlinux.ru> 3.1-alt1.20090312
- New snapshot (3.1 20090312).

* Tue Nov 18 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.4-alt1
- New release (3.0.4).
- Fixed:
  + MFSA 2008-58 Parsing error in E4X default namespace
  + MFSA 2008-57 -moz-binding property bypasses security checks on codebase principals
  + MFSA 2008-56 nsXMLHttpRequest::NotifyEventListeners() same-origin violation
  + MFSA 2008-55 Crash and remote code execution in nsFrameManager
  + MFSA 2008-54 Buffer overflow in http-index-format parser
  + MFSA 2008-53 XSS and JavaScript privilege escalation via session restore
  + MFSA 2008-52 Crashes with evidence of memory corruption (rv:1.9.0.4/1.8.1.18)
  + MFSA 2008-51 file: URIs inherit chrome privileges when opened from chrome
  + MFSA 2008-47 Information stealing via local shortcut files

* Wed Oct 08 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.3-alt1
- New release (3.0.3).
- Firefox set itself as default browser correctly (ALT#17384).
- Reload new plugins.
- Fixed:
  + MFSA 2008-44 resource: traversal vulnerabilities
  + MFSA 2008-43 BOM characters stripped from JavaScript before execution
  + MFSA 2008-42 Crashes with evidence of memory corruption (rv:1.9.0.2/1.8.1.17)
  + MFSA 2008-41 Privilege escalation via XPCnativeWrapper pollution
  + MFSA 2008-40 Forced mouse drag

* Tue Sep 09 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt2
- New bugfix build.
- Update desktop file (ALT#10558).

* Fri Jul 18 2008 Alexey Gladkov <legion@altlinux.ru> 3.0.1-alt1
- New version (3.0.1).
- Fixed:
  + MFSA 2008-36 Crash with malformed GIF file on Mac OS X
  + MFSA 2008-35 Command-line URLs launch multiple tabs when Firefox not running
  + MFSA 2008-34 Remote code execution by overflowing CSS reference counter

* Sun Jul 13 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt2.20080704
- New bugfix build.
- Add searchplugins: bugzilla@altlinux, wikipedia-ru, yandex.
- Remove RPATH.

* Fri Jul 04 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080704
- New cvs snapshot 3.0 (20080704).

* Sat May 31 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080530
- New cvs snapshot 20080530.

* Tue May 20 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.20080519
- New cvs snapshot (3.0 rc1).

* Sun Feb 03 2008 Alexey Gladkov <legion@altlinux.ru> 3.0-alt1.b3pre
- New cvs snapshot.

* Thu Dec 20 2007 Alexey Gladkov <legion@altlinux.ru> 3.0.b2-alt1
- New major beta version 3.0.b2

* Wed Nov 28 2007 Alexey Gladkov <legion@altlinux.ru> 3.0.b1-alt1
- New major beta version 3.0.b1

* Sun Feb 25 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.2-alt1
- New bugfix version 2.0.0.2
- Remove version from requires in *.pc.
- Fixed:
    + MFSA 2007-07  Embedded nulls in location.hostname confuse same-domain checks
    + MFSA 2007-06 Mozilla Network Security Services (NSS) SSLv2 buffer overflow
    + MFSA 2007-05 XSS and local file access by opening blocked popups
    + MFSA 2007-04 Spoofing using custom cursor and CSS3 hotspot
    + MFSA 2007-03 Information disclosure through cache collisions
    + MFSA 2007-02 Improvements to help protect against Cross-Site Scripting attacks
    + MFSA 2007-01 Crashes with evidence of memory corruption (rv:1.8.0.10/1.8.1.2)

* Sun Jan 28 2007 Alexey Gladkov <legion@altlinux.ru> 2.0.0.1-alt1
- New minor version 2.0.0.1
- Fixed:
    + MFSA 2006-76  XSS using outer window's Function object
    + MFSA 2006-75 RSS Feed-preview referrer leak
    + MFSA 2006-73 Mozilla SVG Processing Remote Code Execution
    + MFSA 2006-72 XSS by setting img.src to javascript: URI
    + MFSA 2006-71 LiveConnect crash finalizing JS objects
    + MFSA 2006-70 Privilege escalation using watch point
    + MFSA 2006-69 CSS cursor image buffer overflow (Windows only)
    + MFSA 2006-68 Crashes with evidence of memory corruption (rv:1.8.0.9/1.8.1.1)

* Thu Nov 23 2006 Alexey Gladkov <legion@altlinux.ru> 2.0-alt2
- Add %%pre script.
- Remove version specific paths.

* Sat Oct 28 2006 Alexey Gladkov <legion@altlinux.ru> 2.0-alt1
- New major version 2.0 .
- Don't build libxul.
- Add support for printing via Pango.
- Change printer paper size at A4.
- Check compatibility disabled.
- Patch disabling OS_TEST autoguessing for %%ix86 builds on x86_64 host.

* Fri Sep 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.7-alt1
- New version 1.5.0.7 .
- Fixed:
    + MFSA 2006-64  Crashes with evidence of memory corruption (rv:1.8.0.7)
    + MFSA 2006-62 Popup-blocker cross-site scripting (XSS)
    + MFSA 2006-61 Frame spoofing using document.open()
    + MFSA 2006-60 RSA Signature Forgery
    + MFSA 2006-59 Concurrency-related vulnerability
    + MFSA 2006-58 Auto-Update compromise through DNS and SSL spoofing
    + MFSA 2006-57 JavaScript Regular Expression Heap Corruption

* Wed Aug 30 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt4
- Add libgtkembedmoz.so, firefox-gtkembedmoz.pc .
- Update BuildRequires.

* Wed Aug 16 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt3
- bugfix build.
- Patch to enable intl.locale.matchOS was removed.
- Added default download directory.

* Wed Aug 09 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt2
- bugfix build.
- Added patch to handle #9863 (history #4352).

* Sat Aug 05 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.6-alt1
- New version 1.5.0.6 . 
- Fixed:
    + Fixed an issue with playing Windows Media content
    + MFSA 2006-56  chrome: scheme loading remote content
    + MFSA 2006-55 Crashes with evidence of memory corruption (rv:1.8.0.5)
    + MFSA 2006-54 XSS with XPCNativeWrapper(window).Function(...)
    + MFSA 2006-53 UniversalBrowserRead privilege escalation
    + MFSA 2006-52 PAC privilege escalation using Function.prototype.call
    + MFSA 2006-51 Privilege escalation using named-functions and redefined "new Object()"
    + MFSA 2006-50 JavaScript engine vulnerabilities
    + MFSA 2006-48 JavaScript new Function race condition
    + MFSA 2006-47 Native DOM methods can be hijacked across domains
    + MFSA 2006-46 Memory corruption with simultaneous events
    + MFSA 2006-45 Javascript navigator Object Vulnerability
    + MFSA 2006-44 Code execution through deleted frame reference

* Thu Jun 08 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.4-alt1
- New version.
- Fixed:
    + MFSA 2006-43 Privilege escalation using addSelectionListener
    + MFSA 2006-42 Web site XSS using BOM on UTF-8 pages
    + MFSA 2006-41 File stealing by changing input type (variant)
    + MFSA 2006-39 "View Image" local resource linking (Windows)
    + MFSA 2006-38 Buffer overflow in crypto.signText()
    + MFSA 2006-37 Remote compromise via content-defined setter on object prototypes
    + MFSA 2006-36 PLUGINSPAGE privileged JavaScript execution 2
    + MFSA 2006-35 Privilege escalation through XUL persist
    + MFSA 2006-34 XSS viewing javascript: frames or images from context menu
    + MFSA 2006-33 HTTP response smuggling
    + MFSA 2006-32 Fixes for crashes with potential memory corruption
    + MFSA 2006-31 EvalInSandbox escape (Proxy Autoconfig, Greasemonkey)

* Fri May 12 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.3-alt1
- New version.
- Build libxul library.
- Fixed:
    + MFSA 2006-30 Deleted object reference when designMode="on".

* Wed Mar 15 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.1-alt2
- bugfix build.
- include fix
- plugins directory fix;

* Mon Feb 13 2006 Alexey Gladkov <legion@altlinux.ru> 1.5.0.1-alt1
- New version 1.5.0.1
- Buildrequires updated for xorg-7.0 
- run-firefox script bugfix:
  * usage update
  * plugins search path (x86_64)
  * unparseable commands handling
- bugfix: #7334, #7682, #8757, #8784, #9017

* Sun Dec 04 2005 Alexey Gladkov <legion@altlinux.ru> 1.5-alt1
- New version 1.5 .
- Spec cleanup.
- Build with external rpm-build-firefox .
- Build with system NSS and NSPR.
- Unused libraries removed.
- Rpm mascros bugfix.
  * fix for new rpm.
  * change extension installation sheme (again).
- Default preference tunning.
- Startup script rewritten. Now it is single script.
  * command line shortcut added: altfaq:NUM .
- SVG support enabled.
- directory /usr/share/firefox-@version@/extensions was added to extensions search path .
  * this location is controled by the option extensions.dir.extensions .
- Bug: #7682, #7801, #7856, #7949 fixed.

* Tue Aug 16 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt4
- major bugfix.
- build with official branding.
- x86_64 compatibility addon (patch20, patch21).

* Sun Aug 07 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.6-alt3
- release version.
- firsttime script added.
- SVG support disabled.
- Patch #2 bugfix (bug: #7682)

* Sun Jul 24 2005 LAKostis <lakostis at altlinux.ru> 1.0.6-alt2.cvs
- fix -nox patch.
- add gssapi detection and build fixes from mhz@.

* Tue Jul 19 2005 LAKostis <lakostis at altlinux.ru> 1.0.6-alt1.cvs
- new version from aviary branch fixing various bugs:
  + MFSA2005-54
  + Restore API compatibility for extensions and web applications 
    that did not work in Firefox 1.0.5.
  
* Mon Jul 11 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt2.cvs
- new version from aviary branch;

* Wed Jun 22 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt1.cvs
- new version from aviary branch fixing various security bugs;
- fix: #4846, #5101, #7126 (legion).
- if_{with,without} debug - added (legion).
- keyword 'altbug:' added, patch2 updated (legion).
- postin/postun-scripts scripts bugfixes (legion).
- triggers added for trash cleanup (legion).

* Mon Jun 20 2005 LAKostis <lakostis at altlinux.ru> 1.0.5-alt0.cvs
- new version from aviary branch;
- fix #6595;
- add switches for svg/xprint easy builds.
- update alt-prefs-tuning.patch (disable annoying default browser dialog).

* Sun Jun 12 2005 LAKostis <lakostis at altlinux.ru> 1.0.4-alt1
- new version;
- SA15601 security fix;
- BuildRequires cleanup (remove xorg-x11-libs-static).

* Thu Apr 21 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.3-alt1
- new version;
- requires fix;

* Wed Apr 13 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.2-alt1
- new version;
- RPATH fix;
- NoX patch was rewritten;

* Sun Mar 06 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt2
- rpm macros was updated;

* Fri Feb 25 2005 Alexey Gladkov <legion@altlinux.ru> 1.0.1-alt1
- new version;
- patch9 was added (mozilla Bug #123315);
- patch10, patch11 was added (#6151);

* Mon Feb 14 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt7
- plugins path bugfix;
- svg support added;
- x86_64 compatibility added (thx mouse@);

* Tue Feb 01 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt6
- update patch firefox-1.0-20050201-alt-nox.patch 
  * uninstall-global-theme command-line option was added;
  * update-register command-line option was added;
- firefox-1.0-alt-rpm-scripts.tar.bz2 bugfix;

* Thu Jan 27 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt5
- disable svg support becouse svg layout lead to segfault 
  when mozilla compile with gcc3.4 .
- search plugins was moved into the standalone rpm package.

* Wed Jan 19 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt4
- Rebuilt with libstdc++.so.6.

* Wed Jan 05 2005 Alexey Gladkov <legion@altlinux.ru> 1.0-alt3
- new version;
- browser-plugins-npapi support added;
- new icons default icons(thx shrek@);
- option uninstall-global-extension was fixed;

* Wed Nov 03 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2.rc1
- extension sheme changes;
- postin/preun scripts chenges;

* Mon Oct 18 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt2.PR
- new default extensions added;
- protocol 'mailto' external handler added; 
- firefox.macro changed;
- postun script changed;
- icons changed;

* Thu Sep 30 2004 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1.PR
- New version 1.0PR;
- New extension scheme;
- Add:
    * New option 'run-without-x' added (mouse, legion);
    * SVG support added;
    * Certificate (ALT Linux CA Root) added;
    * ALT Linux BTS search plugin added;
    * RPATH added to all binary files;
- bug #4284 fixed;

* Fri May 28 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt4
- Move back some changes at alt3 build.
- Bug #4157 fixed.

* Fri Apr 30 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt3.1
- viewsource protocol was added.

* Thu Apr 29 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt3
- Minimize buildin extensions;
- Disable debug output;
- Disable some options:
  + disable JavaScript debug library;
  + disable LDAP support;
  + disable logging facilities;
- Necko protocols cleanup;

* Tue Feb 24 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt2
- Splash screen added (thx sadist@);
- Search plugins added;
- Remove devel package Conflicts;
- Change rebuild-database.sh script. Script must be run only as root;
- Change locale hack.

* Wed Feb 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.8-alt1
- Mozilla Firebird becomes Mozilla Firefox. Mozilla's next 
  generation browser has changed names (again);
- New version;

* Sun Jan 11 2004 Alexey Gladkov <legion@altlinux.ru> 0.7-alt2
- Spec changes.
- run-mozilla.sh script patch.

* Tue Dec 30 2003 Alexey Gladkov <legion@altlinux.ru> 0.7-alt1
- first build for ALT Linux.
- rpm macro created.
- new scheme loading extensions added (thx force@)
