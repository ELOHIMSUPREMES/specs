# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
Name:		professor-is-missing
Version:	0.1
Release:	alt4_10
Summary:	The Professor is Missing, an AGI adventure game

Group:		Games/Other
License:	Redistributable, no modification permitted
URL:		http://membres.lycos.fr/agisite/prof.htm
Source0:	prof.zip
#Original from http://membres.lycos.fr/agisite/prof.zip includes
#copyrighted executables. Generated new source by unzipping, removing
#DOS-related content.
Source1:	professor-is-missing.desktop
Source2:	professor-is-missing-wrapper.sh
Source3:	professor-is-missing.xpm
Source4:	professor-is-missing-LICENSE.fedora
BuildArch:	noarch

BuildRequires:	desktop-file-utils
Requires:	nagi icon-theme-hicolor
Source44: import.info

%description
In this little game, for a mysterious reason, the Professor is disaspeared in
Africa. As Eric, you must find a way to go to Africa to find out the
Professor.

%prep

%setup -q -c

#drop case
mv LOGDIR logdir
mv OBJECT object
mv PICDIR picdir
mv SNDDIR snddir
mv VIEWDIR viewdir
mv VOL.0 vol.0
mv WORDS.TOK words.tok

#char fix
sed -i 's/\r//' readme.txt
sed -i 's/\r//' walkthru.txt

%build
cp %{SOURCE4} .

%install

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -D -m0644 -p * $RPM_BUILD_ROOT%{_datadir}/%{name}
install -D -m0755 -p %{SOURCE2} $RPM_BUILD_ROOT/%{_bindir}

# desktop file
desktop-file-install \
	--dir $RPM_BUILD_ROOT%{_datadir}/applications \
	%{SOURCE1}

# icon
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
install -p -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{name}.xpm

%files
%doc readme.txt walkthru.txt professor-is-missing-LICENSE.fedora
%{_datadir}/professor-is-missing
%{_datadir}/applications/professor-is-missing.desktop
%{_datadir}/icons/hicolor/32x32/apps/professor-is-missing.xpm
%{_bindir}/professor-is-missing-wrapper.sh

%changelog
* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_10
- update to new release by fcimport

* Thu Feb 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_9
- update to new release by fcimport

* Fri Jul 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_8
- update to new release by fcimport

* Fri Mar 02 2012 Igor Vlasenko <viy@altlinux.ru> 0.1-alt4_6
- rebuild with fixed sourcedep analyser (#27020)

* Sat May 21 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt3_6
- rebuild to fix .desktop permissions

* Thu May 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt2_6
- rebuild with new rpm desktop cleaner

* Wed Feb 16 2011 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1_6
- converted from Fedora by srpmconvert script

