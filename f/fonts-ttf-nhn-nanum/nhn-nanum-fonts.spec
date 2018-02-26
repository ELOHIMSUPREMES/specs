# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
%define oldname nhn-nanum-fonts
%global fontname nhn-nanum
%global fontconf 65-0-%{fontname}

%global common_version 3.020
%global common_desc \
Nanum fonts are collection of commonly-used Myeongjo and Gothic Korean \
font families, designed by Sandoll Communication and Fontrix. The \
publisher is NHN Corporation.


Name:		fonts-ttf-nhn-nanum
Version:	3.020
Release:	alt5_8
Summary:	Nanum family of Korean TrueType fonts

Group:		System/Fonts/True type
License:	OFL
URL:		http://hangeul.naver.com/share.nhn
Source0:	http://cdn.naver.com/naver/NanumFont/fontfiles/NanumFont_TTF_ALL.zip
Source1:	%{oldname}-brush-fontconfig.conf
Source2:	%{oldname}-gothic-fontconfig.conf
Source3:	%{oldname}-myeongjo-fontconfig.conf
Source4:	%{oldname}-pen-fontconfig.conf
# License text was taken from the upstream web on Nov 21 2012:
# http://help.naver.com/ops/step2/faq.nhn?faqId=15879
Source5:	%{oldname}-license.txt

BuildArch:	noarch
BuildRequires:	fontpackages-devel
Source44: import.info

%description
%common_desc


%package common
Summary:   Common files of %{oldname}
Group:	   System/Fonts/True type

%description common
%common_desc

This package consists of files used by other %{oldname} packages.


%package -n fonts-ttf-nhn-nanum-brush
Group: System/Fonts/True type
Version:	1.100
Summary:	Nanum fonts Brush font faces
Requires:	%{name}-common = %{common_version}-%{release}

%description -n fonts-ttf-nhn-nanum-brush
%common_desc

This package consists of the Nanum fonts Brush font faces.

%files -n fonts-ttf-nhn-nanum-brush
%{_fontconfig_templatedir}/%{fontconf}-brush.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-brush.conf
%{_fontbasedir}/*/%{_fontstem}/NanumBrush.ttf


%package -n fonts-ttf-nhn-nanum-gothic
Group: System/Fonts/True type
Summary:	Nanum fonts Gothic font faces
Requires:	%{name}-common = %{common_version}-%{release}

%description -n fonts-ttf-nhn-nanum-gothic
%common_desc

This package consists of the Nanum fonts Gothic font faces.

%files -n fonts-ttf-nhn-nanum-gothic
%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-gothic.conf
%{_fontbasedir}/*/%{_fontstem}/NanumGothic.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumGothicBold.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumGothicExtraBold.ttf


%package -n fonts-ttf-nhn-nanum-myeongjo
Group: System/Fonts/True type
Summary:	Nanum fonts Myeongjo font faces
Requires:	%{name}-common = %{common_version}-%{release}

%description -n fonts-ttf-nhn-nanum-myeongjo
%common_desc

This package consists of the Nanum fonts Myeongjo font faces.

%files -n fonts-ttf-nhn-nanum-myeongjo
%{_fontconfig_templatedir}/%{fontconf}-myeongjo.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-myeongjo.conf
%{_fontbasedir}/*/%{_fontstem}/NanumMyeongjo.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumMyeongjoBold.ttf
%{_fontbasedir}/*/%{_fontstem}/NanumMyeongjoExtraBold.ttf


%package -n fonts-ttf-nhn-nanum-pen
Group: System/Fonts/True type
Version:	1.100
Summary:	Nanum fonts Pen font faces
Requires:	%{name}-common = %{common_version}-%{release}

%description -n fonts-ttf-nhn-nanum-pen
%common_desc

This package consists of the Nanum fonts Pen font faces.

%files -n fonts-ttf-nhn-nanum-pen
%{_fontconfig_templatedir}/%{fontconf}-pen.conf
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}-pen.conf
%{_fontbasedir}/*/%{_fontstem}/NanumPen.ttf


%prep
%setup -n %{oldname}-%{version} -q -c
cp -p %{SOURCE5} COPYING


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
		   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-brush.conf
install -m 0644 -p %{SOURCE2} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-gothic.conf
install -m 0644 -p %{SOURCE3} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-myeongjo.conf
install -m 0644 -p %{SOURCE4} \
	%{buildroot}%{_fontconfig_templatedir}/%{fontconf}-pen.conf

for fconf in %{fontconf}-brush.conf \
    %{fontconf}-gothic.conf \
    %{fontconf}-myeongjo.conf \
    %{fontconf}-pen.conf ; do
  ln -s %{_fontconfig_templatedir}/$fconf \
     %{buildroot}%{_fontconfig_confdir}/$fconf
done
# generic fedora font import transformations
# move fonts to corresponding subdirs if any
for fontpatt in OTF TTF TTC otf ttf ttc pcf pcf.gz bdf afm pfa pfb; do
    case "$fontpatt" in 
	pcf*|bdf*) type=bitmap;;
	tt*|TT*) type=ttf;;
	otf|OTF) type=otf;;
	afm*|pf*) type=type1;;
    esac
    find $RPM_BUILD_ROOT/usr/share/fonts -type f -name '*.'$fontpatt | while read i; do
	j=`echo "$i" | sed -e s,/usr/share/fonts/,/usr/share/fonts/$type/,`;
	install -Dm644 "$i" "$j";
	rm -f "$i";
	olddir=`dirname "$i"`;
	mv -f "$olddir"/{encodings.dir,fonts.{dir,scale,alias}} `dirname "$j"`/ 2>/dev/null ||:
	rmdir -p "$olddir" 2>/dev/null ||:
    done
done
# kill invalid catalogue links
if [ -d $RPM_BUILD_ROOT/etc/X11/fontpath.d ]; then
    find -L $RPM_BUILD_ROOT/etc/X11/fontpath.d -type l -print -delete ||:
    # relink catalogue
    find $RPM_BUILD_ROOT/usr/share/fonts -name fonts.dir | while read i; do
	pri=10;
	j=`echo $i | sed -e s,$RPM_BUILD_ROOT/usr/share/fonts/,,`; type=${j%%%%/*}; 
	pre_stem=${j##$type/}; stem=`dirname $pre_stem|sed -e s,/,-,g`;
	case "$type" in 
	    bitmap) pri=10;;
	    ttf|ttf) pri=50;;
	    type1) pri=40;;
	esac
	ln -s /usr/share/fonts/$j $RPM_BUILD_ROOT/etc/X11/fontpath.d/"$stem:pri=$pri"
    done ||:
fi


%files common
%doc COPYING


%changelog
* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 3.020-alt5_8
- update to new release by fcimport

* Sat Jan 26 2013 Igor Vlasenko <viy@altlinux.ru> 3.020-alt5_7
- applied repocop patches

* Mon Dec 03 2012 Igor Vlasenko <viy@altlinux.ru> 3.020-alt4_7
- update to new release by fcimport

* Sun Nov 25 2012 Igor Vlasenko <viy@altlinux.ru> 3.020-alt4_6
- converted for ALT Linux by srpmconvert tools

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 3.020-alt4_4
- update to new release by fcimport

* Thu Jul 19 2012 Igor Vlasenko <viy@altlinux.ru> 3.020-alt4_3
- update to new release by fcimport

* Wed Mar 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.020-alt4_1
- rebuild to get rid of #27020

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.020-alt3_1
- new fc release

* Tue Feb 21 2012 Igor Vlasenko <viy@altlinux.ru> 3.020-alt1_1
- update to new release by fcimport

* Wed Feb 01 2012 Igor Vlasenko <viy@altlinux.ru> 3.010-alt2_2
- update to new release by fcimport

* Wed Aug 24 2011 Igor Vlasenko <viy@altlinux.ru> 3.010-alt2_1
- rebuild with new rpm-build-fonts

* Sat Aug 06 2011 Igor Vlasenko <viy@altlinux.ru> 3.010-alt1_1
- initial release by fcimport

