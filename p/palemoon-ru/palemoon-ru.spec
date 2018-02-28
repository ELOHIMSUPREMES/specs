%define cid            langpack-ru@palemoon.org
%define cid_dir        %palemoon_noarch_extensionsdir/%cid

%define cid_dict       ru@dictionaries.addons.mozilla.org
%define cid_dict_dir   %palemoon_noarch_extensionsdir/%cid_dict

%define min_version	27.1.99
%define max_version	27.*

%define bname		newmoon
%define sdir		searchplugins
%define newmoon_dir 	%_datadir/%bname-data/browser/
%define search_dir 	%newmoon_dir%sdir

Name: palemoon-ru
Version: 27.2.0
Release: alt2

Summary: Russian (RU) Language Pack for Pale Moon
License: MPL/GPL/LGPL

Group: Networking/WWW
Url: http://www.palemoon.org/langpacks.shtml
BuildArch: noarch

Packager: Hihin Ruslan <ruslandh@altlinux.ru>

Source:  ru_palemoon_%version.xpi
Source2: searchplugins.tar
Patch:   %name-27.1.1-search.patch
Patch1:	 %name-27.2.0-version.patch
Patch2:	 %name-27.2.0-advanced.patch

Requires: palemoon >= %version
Requires: hunspell-ru
Obsoletes: palemoon-ru_yo-dictionary palemoon-ru_ie-dictionary
Provides: palemoon-ru_yo-dictionary palemoon-ru_ie-dictionary

BuildRequires(pre):	rpm-build-palemoon 
# Automatically added by buildreq on Mon Jul 13 2015
BuildRequires: libdb4-devel unzip

%description
The Palemoon Russian translation and dictionary.

%package -n palemoon-searchplugins
Summary: The Palemoon Russian translation and dictionary.
Group:   Networking/WWW
BuildArch: noarch
Conflicts:  palemoon-ru < %EVR

%description -n palemoon-searchplugins
The set of search plugins for Palemoon

%description -n palemoon-searchplugins -l ru_RU.UTF8
Набор Поисковых плагинов для Palemoon


%prep
%setup -c -n %name-%version/%cid
%patch -p2
%patch1 -p2
%patch2 -p2

tar -xf %SOURCE2



%install
cd ..

mkdir -p -- \
	%buildroot/%cid_dir \
	%buildroot/%cid_dict_dir/dictionaries

install -d -m 755 %buildroot/%newmoon_dir/

# Install translation
cp -r -- %cid/* %buildroot/%cid_dir


cd -

cp -r -- %sdir  %buildroot/%search_dir/


#sed -r -i \
#    -e 's,<em:maxVersion>4.0</em:maxVersion>,<em:maxVersion>4.*</em:maxVersion>,g' \
#    -e 's,<em:minVersion>4.0</em:minVersion>,<em:minVersion>4.0</em:minVersion>,g' \
#    %buildroot/%cid_dir/install.rdf

# Install dictionary
cat > %buildroot/%cid_dict_dir/install.rdf <<-EOF
	<?xml version="1.0"?>
	<RDF xmlns="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
	     xmlns:em="http://www.mozilla.org/2004/em-rdf#">
	  <Description about="urn:mozilla:install-manifest"
	               em:id="%cid_dict"
	               em:name="Russian (RU) Dictionary"
	               em:version="%version"
	               em:type="64"
	               em:unpack="true"
	               em:creator="Mozilla Russia">
	    <em:targetApplication>
	      <Description>
	        <em:id>{8de7fcbb-c55c-4fbe-bfc5-fc555c87dbc4}</em:id>
	        <em:minVersion>%min_version</em:minVersion>
	        <em:maxVersion>%max_version.*</em:maxVersion>
	      </Description>
	    </em:targetApplication>
	  </Description>
	</RDF>
EOF
ln -s %_datadir/myspell/ru_RU.aff %buildroot/%cid_dict_dir/dictionaries/ru.aff
ln -s %_datadir/myspell/ru_RU.dic %buildroot/%cid_dict_dir/dictionaries/ru.dic


%files
%cid_dir
%cid_dict_dir

%files -n palemoon-searchplugins
%search_dir

%changelog
* Mon Apr 10 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.2.0-alt2
- Add the set of search plugins for Palemoon

* Sat Mar 18 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.2.0-alt1
- Version 27.2.0-RC1

* Fri Feb 24 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.1.1-alt2.RC1
- Fix searchplugins

* Wed Feb 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.1.1-alt1.RC1
- Add Russian searchplugins

* Wed Feb 22 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.1.1-alt0.RC1
- Version 27.1.1-RC1

* Mon Feb 06 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.1.0-alt0.RC1
- Version 27.1.0-RC1

* Sat Jan 14 2017 Hihin Ruslan <ruslandh@altlinux.ru> 27.0.3-alt2
- Update from https://github.com/JustOff/pale-moon-localization.git

* Fri Dec 23 2016 Hihin Ruslan <ruslandh@altlinux.ru> 27.0.3-alt1
- Version 27.0.3 (ALT #32932)

* Thu Dec 01 2016 Hihin Ruslan <ruslandh@altlinux.ru> 27.0.0-alt1
- Version 27.0.0

* Thu Feb 11 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0.1-alt5
- Fix Translate

* Fri Feb 05 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0.1-alt4.1
- Fix Version

* Wed Jan 27 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0-alt4
- Fix install.rdf

* Sun Jan 24 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0-alt3
- Add translats

* Fri Jan 15 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0-alt2
- Add translats

* Sun Jan 10 2016 Hihin Ruslan <ruslandh@altlinux.ru> 26.0-alt1
- New Version

* Sat Nov 21 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.6-alt1
- New Version

* Tue Sep 01 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.4-alt2
- Fix search

* Thu Jul 16 2015 Hihin Ruslan <ruslandh@altlinux.ru> 25.4-alt1
- initial build for ALT Linux Sisyphus



