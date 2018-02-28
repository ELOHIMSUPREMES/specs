%brp_strip_none %_bindir/*
%brp_strip_none %browser_plugins_path/*
%set_verify_elf_method textrel=relaxed
%def_enable include_x86_64

Name: adobe-flash-player
%define bin_name mozilla-plugin-adobe-flash
%define ver_fake   11
%define ver_ix86   11.2.202.521
%define ver_x86_64 11.2.202.521
Release: alt53
Serial: 3

%define ver_real %ver_fake
%ifarch x86_64
%define ver_real %ver_x86_64
%endif
%ifarch %ix86
%define ver_real %ver_ix86
%endif
Version: %ver_fake

Group: Networking/WWW
Summary: Adobe Flash Player
URL: http://www.adobe.com/products/flashplayer/
License: Commercial

ExclusiveArch: %ix86 x86_64
BuildRequires: rpm-macros-browser-plugins libXt libgtk+2-devel fontconfig desktop-file-utils

Source: LICENSE
Source2: adobe_flash_player_eula.desktop.in
#
Source10: flash_player-x86_64-%ver_x86_64.tar
Source11: flash_player-x86-%ver_ix86.tar

%description
Adobe Flash Player %version (Macromedia Flash)
Fully Supported: Mozilla 1.0+, Netscape 7.x, Firefox 0.8+
Partially Supported: Opera, Konqueror 3.x

See the end user license in
  %_docdir/%name-%version/LICENSE.txt
See the distribution license in
  http://www.adobe.com/licensing/distribution/license/

%package -n %bin_name
Version: %ver_real
Group: Networking/WWW
Summary: Adobe Flash Player
Requires: libcurl /usr/bin/xdg-open
Provides: flash-plugin = %version-%release
Obsoletes: flash-plugin <= %version
Provides: mozilla-plugin-macromedia-flash = %version-%release
Obsoletes: mozilla-plugin-macromedia-flash < %version-%release
%description -n %bin_name
Adobe Flash Player %version (Macromedia Flash)
Fully Supported: Mozilla 1.0+, Netscape 7.x, Firefox 0.8+
Partially Supported: Opera, Konqueror 3.x

See the end user license in
  %_docdir/%name-%version/LICENSE.txt
See the distribution license in
  http://www.adobe.com/licensing/distribution/license/

%package fake
Version: %ver_fake
Group: Networking/WWW
Summary: fake
%description fake
fake


%prep
%setup -Tqcn flash_player_%{version}_linux
%ifarch x86_64
%if_enabled include_x86_64
tar xfv %SOURCE10
%endif
%else
tar xfv %SOURCE11
%endif
install -m 0644 %SOURCE0 LICENSE.txt


%build

%install
mkdir -p -m 0755 %buildroot/%browser_plugins_path
%ifarch x86_64
%if_enabled include_x86_64
install -m 0644 libflashplayer.so %buildroot/%browser_plugins_path
%endif
%else
install -m 0644 libflashplayer.so %buildroot/%browser_plugins_path
%endif

# install flash-player-properties
mkdir -p %buildroot/{%_bindir,%_desktopdir,%_miconsdir,%_niconsdir,%_liconsdir}
install -m0755 ./%_bindir/flash-player-properties %buildroot/%_bindir/
desktop-file-install -m 0644 --dir %buildroot/%_desktopdir \
    --add-category=X-PersonalSettings \
    --remove-key=NotShowIn \
    ./%_desktopdir/flash-player-properties.desktop
for icondir in %_miconsdir %_niconsdir %_liconsdir
do
    install -m 0644 ./$icondir/flash-player-properties.png %buildroot/$icondir/
done


# menu
mkdir -p -m0755 %buildroot/%_desktopdir
cat %SOURCE2 | sed 's|%%LICENSE_PATH%%|%{_docdir}/%{bin_name}-%{ver_real}/LICENSE.txt|' > adobe_flash_player_eula.desktop
install -m0644 adobe_flash_player_eula.desktop %buildroot/%_desktopdir/

%ifarch x86_64
%if_disabled include_x86_64
%post -n %bin_name
echo "At this moment you must install manually nspluginwrapper and i586-%name (see bugs 23876 23877 23878 23903)"
%endif
%endif

%files -n %bin_name
%_bindir/flash-player-properties
%_desktopdir/flash-player-properties.desktop
%_iconsdir/hicolor/*/apps/flash-player-properties.*
#
%ifarch x86_64
%if_enabled include_x86_64
%doc LICENSE*
%browser_plugins_path/*
%_desktopdir/adobe_flash_player_eula.desktop
%endif
%else
%doc LICENSE*
%browser_plugins_path/*
%_desktopdir/adobe_flash_player_eula.desktop
%endif

%changelog
* Fri Sep 25 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt53
- new version
- security fixes:
  CVE-2015-5567, CVE-2015-5568, CVE-2015-5570, CVE-2015-5571,
  CVE-2015-5572, CVE-2015-5573, CVE-2015-5574, CVE-2015-5575,
  CVE-2015-5576, CVE-2015-5577, CVE-2015-5578, CVE-2015-5579,
  CVE-2015-5580, CVE-2015-5581, CVE-2015-5582, CVE-2015-5584,
  CVE-2015-5587, CVE-2015-5588, CVE-2015-6676, CVE-2015-6677,
  CVE-2015-6678, CVE-2015-6679, CVE-2015-6682

* Wed Aug 12 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt52
- new version
- security fixes:
  CVE-2015-3107, CVE-2015-5124, CVE-2015-5125, CVE-2015-5127,
  CVE-2015-5128, CVE-2015-5129, CVE-2015-5130, CVE-2015-5131,
  CVE-2015-5132, CVE-2015-5133, CVE-2015-5134, CVE-2015-5539,
  CVE-2015-5540, CVE-2015-5541, CVE-2015-5544, CVE-2015-5545,
  CVE-2015-5546, CVE-2015-5547, CVE-2015-5548, CVE-2015-5549,
  CVE-2015-5550, CVE-2015-5551, CVE-2015-5552, CVE-2015-5553,
  CVE-2015-5554, CVE-2015-5555, CVE-2015-5556, CVE-2015-5557,
  CVE-2015-5558, CVE-2015-5559, CVE-2015-5560, CVE-2015-5561,
  CVE-2015-5562, CVE-2015-5563, CVE-2015-5564

* Sat Jul 18 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt51
- new version
- security fixes: CVE-2015-5122, CVE-2015-5123

* Tue Jul 14 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt50
- fix changelog
- security NOT fixed: CVE-2015-5122, CVE-2015-5123

* Mon Jul 13 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt49
- update changelog

* Wed Jul 08 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt48
- update changelog

* Wed Jul 08 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt47
- new version
- security fixes:
  CVE-2014-0578, CVE-2015-3097, CVE-2015-3114, CVE-2015-3115,
  CVE-2015-3116, CVE-2015-3117, CVE-2015-3118, CVE-2015-3119,
  CVE-2015-3120, CVE-2015-3121, CVE-2015-3122, CVE-2015-3123,
  CVE-2015-3124, CVE-2015-3125, CVE-2015-3126, CVE-2015-3127,
  CVE-2015-3128, CVE-2015-3129, CVE-2015-3130, CVE-2015-3131,
  CVE-2015-3132, CVE-2015-3133, CVE-2015-3134, CVE-2015-3135,
  CVE-2015-3136, CVE-2015-3137, CVE-2015-4428, CVE-2015-4429,
  CVE-2015-4430, CVE-2015-4431, CVE-2015-4432, CVE-2015-4433,
  CVE-2015-5116, CVE-2015-5117, CVE-2015-5118, CVE-2015-5119

* Wed Jun 24 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt46
- new version
- security fixes: CVE-2015-3113

* Wed Jun 10 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt45
- new version
- security fixes:
  CVE-2015-3096, CVE-2015-3097, CVE-2015-3098, CVE-2015-3099,
  CVE-2015-3100, CVE-2015-3101, CVE-2015-3102, CVE-2015-3103,
  CVE-2015-3104, CVE-2015-3105, CVE-2015-3106, CVE-2015-3107,
  CVE-2015-3108

* Thu May 14 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt44
- new version
- security fixes:
  CVE-2015-3044, CVE-2015-3077, CVE-2015-3078, CVE-2015-3079,
  CVE-2015-3080, CVE-2015-3081, CVE-2015-3082, CVE-2015-3083,
  CVE-2015-3084, CVE-2015-3085, CVE-2015-3086, CVE-2015-3087,
  CVE-2015-3088, CVE-2015-3089, CVE-2015-3090, CVE-2015-3091,
  CVE-2015-3092, CVE-2015-3093

* Wed Apr 15 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt43
- new version
- security fixes:
  CVE-2015-0346, CVE-2015-0347, CVE-2015-0348, CVE-2015-0349,
  CVE-2015-0350, CVE-2015-0351, CVE-2015-0352, CVE-2015-0353,
  CVE-2015-0354, CVE-2015-0355, CVE-2015-0356, CVE-2015-0357,
  CVE-2015-0358, CVE-2015-0359, CVE-2015-0360, CVE-2015-3038,
  CVE-2015-3039, CVE-2015-3040, CVE-2015-3041, CVE-2015-3042,
  CVE-2015-3043, CVE-2015-3044

* Fri Mar 13 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt42
- new version
- security fixes:
  CVE-2015-0332, CVE-2015-0333, CVE-2015-0334, CVE-2015-0335,
  CVE-2015-0336, CVE-2015-0337, CVE-2015-0338, CVE-2015-0339,
  CVE-2015-0340, CVE-2015-0341, CVE-2015-0342

* Fri Feb 06 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt41
- new version
- security fixes:
  CVE-2015-0313, CVE-2015-0314, CVE-2015-0315, CVE-2015-0316,
  CVE-2015-0317, CVE-2015-0318, CVE-2015-0319, CVE-2015-0320,
  CVE-2015-0321, CVE-2015-0322, CVE-2015-0323, CVE-2015-0324,
  CVE-2015-0325, CVE-2015-0326, CVE-2015-0327, CVE-2015-0328,
  CVE-2015-0329, CVE-2015-0330

* Wed Jan 28 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt40
- new version
- security fixes: CVE-2015-0311, CVE-2015-0312

* Fri Jan 23 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt39
- new version
- security fixes: CVE-2015-0310, CVE-2015-0311

* Wed Jan 14 2015 Sergey V Turchin <zerg@altlinux.org> 3:11-alt38
- new version
- security fixes:
  CVE-2015-0301, CVE-2015-0302, CVE-2015-0303, CVE-2015-0304,
  CVE-2015-0305, CVE-2015-0306, CVE-2015-0307, CVE-2015-0308,
  CVE-2015-0309

* Wed Dec 10 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt37
- new version
- security fixes:
  CVE-2014-0580, CVE-2014-0587, CVE-2014-8443, CVE-2014-9162,
  CVE-2014-9163, CVE-2014-9164

* Wed Nov 26 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt36
- new version
- security fixes: CVE-2014-8439

* Wed Nov 12 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt35
- new version
- security fixes:
  CVE-2014-0573, CVE-2014-0574, CVE-2014-0576, CVE-2014-0577,
  CVE-2014-0581, CVE-2014-0582, CVE-2014-0583, CVE-2014-0584,
  CVE-2014-0585, CVE-2014-0586, CVE-2014-0588, CVE-2014-0589,
  CVE-2014-0590, CVE-2014-8437, CVE-2014-8438, CVE-2014-8440,
  CVE-2014-8441, CVE-2014-8442

* Wed Oct 15 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt34
- new version
- security fixes: CVE-2014-0570, CVE-2014-0571, CVE-2014-0572

* Wed Sep 10 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt33
- new version
- security fixes:
  CVE-2014-0547, CVE-2014-0548, CVE-2014-0549, CVE-2014-0550,
  CVE-2014-0551, CVE-2014-0552, CVE-2014-0553, CVE-2014-0554,
  CVE-2014-0555, CVE-2014-0556, CVE-2014-0557, CVE-2014-0559

* Mon Aug 18 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt32
- new version
- security fixes:
  CVE-2014-0538, CVE-2014-0540, CVE-2014-0541, CVE-2014-0542,
  CVE-2014-0543, CVE-2014-0544, CVE-2014-0545

* Wed Jul 16 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt31
- new version (ALT#30190)
- security fixes: CVE-2014-0537, CVE-2014-0539, CVE-2014-4671

* Mon Jun 16 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt30
- new version
- security fixes:
  CVE-2014-0531, CVE-2014-0532, CVE-2014-0533, CVE-2014-0534,
  CVE-2014-0535, CVE-2014-0536

* Tue Apr 29 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt29
- new version
- security fixes: CVE-2014-0515

* Tue Apr 15 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt28
- new version
- security fixes:
  CVE-2014-0506, CVE-2014-0507, CVE-2014-0508, CVE-2014-0509

* Thu Mar 13 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt27
- new version
- security fixes: CVE-2014-0503, CVE-2014-0504

* Fri Feb 21 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt26
- new version
- security fixes: CVE-2014-0498, CVE-2014-0499, CVE-2014-0502

* Wed Feb 05 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt25
- new version
- security fixes: CVE-2014-0497

* Fri Jan 24 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt24
- 11.2.202.335 (x86,x86-64)
- security fixes:
  CVE-2014-0491, CVE-2014-0492

* Thu Jan 09 2014 Sergey V Turchin <zerg@altlinux.org> 3:11-alt23
- 11.2.202.332 (x86,x86-64)
- security fixes:
  CVE-2013-5331, CVE-2013-5332

* Wed Nov 20 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt22
- 11.2.202.327 (x86,x86-64)
- security fixes:
  CVE-2013-5329, CVE-2013-5330

* Wed Sep 11 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt21
- 11.2.202.310 (x86,x86-64)
- security fixes:
  CVE-2013-3361, CVE-2013-3362, CVE-2013-3363, CVE-2013-5324

* Tue Jul 16 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt20
- 11.2.202.297 (x86,x86-64)
- security fixes: CVE-2013-3344, CVE-2013-3345, CVE-2013-3347

* Mon Jun 17 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt19
- 11.2.202.291 (x86,x86-64)
- security fixes: CVE-2013-3343

* Mon Jun 03 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt18
- 11.2.202.285 (x86,x86-64)
- security fixes:
  CVE-2013-2728, CVE-2013-3324, CVE-2013-3325, CVE-2013-3326,
  CVE-2013-3327, CVE-2013-3328, CVE-2013-3329, CVE-2013-3330,
  CVE-2013-3331, CVE-2013-3332, CVE-2013-3333, CVE-2013-3334,
  CVE-2013-3335

* Thu Apr 11 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt17
- 11.2.202.280 (x86,x86-64)
- security fixes:
  CVE-2013-1378, CVE-2013-1379, CVE-2013-1380, CVE-2013-2555

* Thu Feb 28 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt16
- 11.2.202.273 (x86,x86-64)
- security fixes:
  CVE-2013-0504, CVE-2013-0643, CVE-2013-0648

* Mon Feb 11 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt15
- 11.2.202.262 (x86,x86-64)
- security fixes:
  CVE-2013-0633, CVE-2013-0634

* Fri Jan 11 2013 Sergey V Turchin <zerg@altlinux.org> 3:11-alt14
- 11.2.202.261 (x86,x86-64)
- security fixes:
  CVE-2013-0630

* Wed Dec 12 2012 Sergey V Turchin <zerg@altlinux.org> 3:11-alt13
- 11.2.202.258 (x86,x86-64)

* Thu Oct 11 2012 Sergey V Turchin <zerg@altlinux.org> 3:11-alt12
- 11.2.202.243 (x86,x86-64)
- security fixes:
  CVE-2012-5248, CVE-2012-5249, CVE-2012-5250, CVE-2012-5251,
  CVE-2012-5252, CVE-2012-5253, CVE-2012-5254, CVE-2012-5255,
  CVE-2012-5256, CVE-2012-5257, CVE-2012-5258, CVE-2012-5259,
  CVE-2012-5260, CVE-2012-5261, CVE-2012-5262, CVE-2012-5263,
  CVE-2012-5264, CVE-2012-5265, CVE-2012-5266, CVE-2012-5267,
  CVE-2012-5268, CVE-2012-5269, CVE-2012-5270, CVE-2012-5271,
  CVE-2012-5272

* Wed Aug 15 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt11
- security fixes:
  CVE-2012-1535

* Wed Jun 13 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt10
- security fixes:
  CVE-2012-2034, CVE-2012-2035, CVE-2012-2036, CVE-2012-2037,
  CVE-2012-2038, CVE-2012-2039, CVE-2012-2040

* Thu May 10 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt9
- 11.2.202.235 (x86,x86-64)
  CVE-2012-0779

* Mon Apr 02 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt8
- 11.2.202.228 (x86,x86-64)

* Sun Mar 11 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt7
- CVE-2012-0768, CVE-2012-0769

* Thu Feb 16 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt5.M60P.1
- built for M60P

* Thu Feb 16 2012 Sergey V Turchin <zerg@altlinux.org> 2:11-alt6
- 11.1.102.62 (x86,x86-64)
- security fixes:
  CVE-2012-0751, CVE-2012-0752, CVE-2012-0753, CVE-2012-0754,
  CVE-2012-0755, CVE-2012-0756, CVE-2012-0767

* Thu Dec 01 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt4.M60P.1
- built for M60P

* Thu Dec 01 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt5
- update license text

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt3.M60P.1
- built for M60P

* Fri Nov 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt4
- 11.1.102.55 (x86,x86-64)
- security fixes:
  CVE-2011-2445, CVE-2011-2450, CVE-2011-2451, CVE-2011-2452,
  CVE-2011-2453, CVE-2011-2454, CVE-2011-2455, CVE-2011-2456,
  CVE-2011-2457, CVE-2011-2458, CVE-2011-2459, CVE-2011-2460

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt2.M60P.1
- built for M60P

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt3
- 11.0.1.152 (x86,x86-64)

* Thu Oct 06 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt2
- use brp_strip_none instead of set_strip_method

* Mon Sep 26 2011 Sergey V Turchin <zerg@altlinux.org> 2:11-alt1
- 11.0.1.129 (x86,x86-64)

* Fri Aug 26 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt13
- new version 11.0.1.98(x86)

* Fri Aug 12 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt11.M51.1
- built for M51

* Thu Aug 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt12
- new version 10.3.183.5(x86), 11.0.1.98(x86-64)
- security fixes:
  CVE-2011-2130, CVE-2011-2134, CVE-2011-2135, CVE-2011-2136,
  CVE-2011-2137, CVE-2011-2138, CVE-2011-2139, CVE-2011-2140,
  CVE-2011-2414, CVE-2011-2415, CVE-2011-2416, CVE-2011-2417,
  CVE-2011-2425

* Thu Jul 14 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt11
- new beta 11.0.1.60 (64-bit only)

* Tue Jun 07 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt9.M51.1
- built for M51

* Mon Jun 06 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt10
- new version 10.3.181.22 (32-bit only)

* Sun May 29 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt9
- fix path to LICENSE.txt

* Fri May 20 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt8
- fix desktop-file premissions

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt6.M51.1
- build for M51

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt7
- package flash-player-properties

* Mon May 16 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt6
- new version 10.3.181.14(x86-32)
- only 32-bit security fixes:
  CVE-2011-0579, CVE-2011-0618, CVE-2011-0619, CVE-2011-0620,
  CVE-2011-0621, CVE-2011-0622, CVE-2011-0623, CVE-2011-0624,
  CVE-2011-0625, CVE-2011-0626, CVE-2011-0627

* Mon Apr 18 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt4.M51.1
- build for M51

* Mon Apr 18 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt5
- new version 10.2.159.1(x86-32)

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt3.M51.1
- build for M51

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt4
- fix build requires

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt2.M51.1
- build for M51

* Mon Apr 11 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt3
- new version 10.2.153.1(x86-32)

* Tue Feb 15 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt1.M51.1
- build for M51

* Mon Feb 14 2011 Sergey V Turchin <zerg@altlinux.org> 2:10-alt2
- new version 10.2.152.27(x86-32)

* Mon Dec 06 2010 Sergey V Turchin <zerg@altlinux.org> 1:10-alt0.M51.1
- built for M51

* Fri Dec 03 2010 Sergey V Turchin <zerg@altlinux.org> 1:10-alt1
- new version
- package different versions for ix86(10.1.102.65) and x86_64(10.3.162.29)

* Thu Sep 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.23-alt0.M51.1
- built for M51

* Thu Sep 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.23-alt1
- CVE-2010-2884

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.22-alt0.M51.1
- built for M51

* Thu Sep 16 2010 Sergey V Turchin <zerg@altlinux.org> 10.2.161.22-alt1
- 10.2.161.22 beta
- package 64-bit version too

* Mon Aug 30 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt3
- fix conflicts with i586-%name

* Wed Aug 18 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt2
- don't package 64-bit version

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt0.M51.1
- built for M51

* Wed Aug 11 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.82.76-alt1
- only 32-bit new version
- CVE-2010-0209 CVE-2010-2188 CVE-2010-2213 CVE-2010-2214 CVE-2010-2215
  CVE-2010-2216

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.53.64-alt0.M51.1
- built for M51

* Mon Jun 14 2010 Sergey V Turchin <zerg@altlinux.org> 10.1.53.64-alt1
- only 32-bit new version (ALT#17168)
- only 32-bit fixes CVE-2008-4546 CVE-2009-3793 CVE-2010-1297 CVE-2010-2160
  CVE-2010-2161 CVE-2010-2162 CVE-2010-2163 CVE-2010-2164 CVE-2010-2165
  CVE-2010-2166 CVE-2010-2167 CVE-2010-2169 CVE-2010-2170 CVE-2010-2171
  CVE-2010-2172 CVE-2010-2173 CVE-2010-2174 CVE-2010-2175 CVE-2010-2176
  CVE-2010-2177 CVE-2010-2178 CVE-2010-2179 CVE-2010-2180 CVE-2010-2181
  CVE-2010-2182 CVE-2010-2183 CVE-2010-2184 CVE-2010-2185 CVE-2010-2186
  CVE-2010-2187 CVE-2010-2188 CVE-2010-2189

* Wed Feb 17 2010 Sergey V Turchin <zerg@altlinux.org> 10.0.45.2-alt0.M51.1
- built for M51

* Wed Feb 17 2010 Sergey V Turchin <zerg@altlinux.org> 10.0.45.2-alt1
- new version
- fix requires

* Wed Dec 09 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.42.34-alt0.M51.1
- built for M51

* Wed Dec 09 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.42.34-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt4
- fix requires

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt3
- don't use old netscape plugins placement

* Mon Sep 28 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt2
- move to more accessible place

* Tue Aug 11 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.32.18-alt1
- new version

* Thu Jun 25 2009 Sergey V Turchin <zerg@altlinux.org> 10.0.22.87-alt2
- add x86_64 version

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 10.0.22.87-alt0.M41.1
- built for M41

* Fri Feb 27 2009 Sergey V Turchin <zerg at altlinux dot org> 10.0.22.87-alt1
- security update (SA34012)

* Fri Dec 19 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.15.3-alt1
- new version
- remove deprecated macroses from specfile

* Fri Oct 31 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.12.36-alt2
- add libcurl to requires

* Wed Oct 15 2008 Sergey V Turchin <zerg at altlinux dot org> 10.0.12.36-alt1
- new version

* Thu Apr 10 2008 Sergey V Turchin <zerg at altlinux dot org> 9.0.124.0-alt2
- fix src tarball file permissions

* Wed Dec 05 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.115.0-alt1
- new version

* Fri Aug 17 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt3
- fix path to license in desktop-file

* Thu Jul 12 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt2
- add Categories parameter to desktop-file

* Thu Jul 12 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.48.0-alt1
- new version

* Mon Jan 22 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.31.0-alt2
- fix license && package description

* Fri Jan 19 2007 Sergey V Turchin <zerg at altlinux dot org> 9.0.31.0-alt1
- release 9.0.31.0

* Thu Oct 26 2006 Sergey V Turchin <zerg at altlinux dot org> 9.0.21.55-alt0.1.beta
- new beta version

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 7.0.63-alt1
- new version

* Wed Dec 28 2005 Sergey V Turchin <zerg at altlinux dot org> 7.0.61-alt1
- new version

* Thu Jan 06 2005 Alexey Gladkov <legion@altlinux.ru> 7.0.25-alt1.1
- browser-plugins-npapi support added;

* Fri May 28 2004 Sergey V Turchin <zerg at altlinux dot org> 7.0.25-alt1
- new version

* Thu May 27 2004 Sergey V Turchin <zerg at altlinux dot org> 6.0.81-alt2
- fix menu section

* Tue May 25 2004 Sergey V Turchin <zerg at altlinux dot org> 6.0.81-alt1
- new version
- add menufile to show license

* Fri Aug 01 2003 Sergey V Turchin <zerg at altlinux dot org> 6.0.79-alt1
- new version

* Tue Feb 11 2003 Sergey V Turchin <zerg@altlinux.ru> 6.0.69-alt1
- initial spec
