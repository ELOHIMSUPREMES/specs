Group: System/Fonts/True type
%define oldname adobe-source-sans-pro-fonts
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global fontname source-sans-pro
%global fontconf 63-%{fontname}.conf

%global roman_version 2.020
%global italic_version 1.075
%global github_tag %{roman_version}R-ro/%{italic_version}R-it
%global source_dir %{fontname}-%(tr "/" "-" <<<%{github_tag})

Name:           fonts-otf-adobe-source-sans-pro
Version:        %{roman_version}
Release:        alt1_1
Summary:        A set of OpenType fonts designed for user interfaces

License:        OFL
URL:            https://github.com/adobe-fonts/source-sans-pro
#unable to build from source: source format is unbuildable with free software
Source0:        https://github.com/adobe-fonts/source-sans-pro/archive/%{github_tag}/%{oldname}-%{version}.tar.gz
Source1:        %{oldname}-fontconfig.conf
Source2:        %{fontname}.metainfo.xml

BuildRequires:  fontpackages-devel
BuildArch:      noarch
Source44: import.info

%description
Source Sans is a set of OpenType fonts that have been designed to work well in
user interface (UI) environments, as well as in text setting for screen and
print.


%prep
%setup -q -n %{source_dir}


# Fix permissions
chmod 0644 LICENSE.txt README.md

# Fix wrong EOLs
sed -i.orig "s/\r//" LICENSE.txt && \
touch -r LICENSE.txt.orig LICENSE.txt && \
rm LICENSE.txt.orig


%build


%install
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p OTF/*.otf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fontconf}
ln -s %{_fontconfig_templatedir}/%{fontconf} \
      %{buildroot}%{_fontconfig_confdir}/%{fontconf}

# Add AppStream metadata
install -Dm 0644 -p %{SOURCE2} \
        %{buildroot}%{_datadir}/appdata/%{fontname}.metainfo.xml
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


%files
%{_fontconfig_templatedir}/%{fontconf}
%config(noreplace) %{_fontconfig_confdir}/%{fontconf}
%{_fontbasedir}/*/%{_fontstem}/*.otf
%doc README.md
%doc LICENSE.txt
%{_datadir}/appdata/%{fontname}.metainfo.xml


%changelog
* Mon Oct 23 2017 Igor Vlasenko <viy@altlinux.ru> 2.020-alt1_1
- update to new release by fcimport

* Thu Jul 10 2014 Igor Vlasenko <viy@altlinux.ru> 1.065-alt1_0
- new version 2.010roman-1.065-italic

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.050-alt1_3
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.050-alt1_2
- update to new release by fcimport

* Sat May 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.050-alt1_1
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.034-alt1_2
- update to new release by fcimport

* Mon Nov 05 2012 Igor Vlasenko <viy@altlinux.ru> 1.034-alt1_1
- fc import

