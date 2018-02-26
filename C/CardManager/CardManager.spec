# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           CardManager
Version:        1
Release:        alt1_2jpp7
Summary:        Java application to allows you to play any, especially collectible, card game

Group:          Games/Other
License:        BSD
URL:            http://cardmanager.wz.cz/
Source0:        http://cardmanager.wz.cz/CardManager_sources.zip
Patch0:         removeManifestEntries.patch
BuildArch:      noarch

BuildRequires:  jpackage-utils
BuildRequires:  ant
BuildRequires:  ant-nodeps
BuildRequires:  desktop-file-utils

Requires:       jpackage-utils
Source44: import.info

%description
This is free, open source multiplatform (java) application which allows you to
 play ANY card game. 
The game is designed especially to play collectible card games like Magic the
 Gathering or Doomtrooper over network.
To play those games you need to own (scanned) images of card, which are not part
 of this package.
Some can be easily downloadable from internet, but be aware of copyrights.
The default deck and background is free of copyright
Also please feel free to add your own backgrounds to 
~/CardManager/data/backgrounds and of course enhance
collection under ~/CardManager/collection

%package javadoc
Summary:        Javadocs for %{name}
Group:          Development/Java
Requires:       jpackage-utils
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -c CardManager
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
%patch0

%build

ant

%install

#desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  CardManager.desktop
cp -p ./CardManager.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/
#end desktop

#launcher
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -p ./FedoraLauncher.sh $RPM_BUILD_ROOT%{_bindir}/CardManager
#end launcher



mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r data $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r collection $RPM_BUILD_ROOT/%{_datadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_datadir}/pixmaps/CardManager.png
%{_datadir}/applications/CardManager.desktop
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/CardManager
%{_javadir}/*
%doc license.txt

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt


%changelog
* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 1-alt1_2jpp7
- new version

