# BEGIN SourceDeps(oneline):
BuildRequires: perl(B.pm) perl(Config.pm) perl(Devel/Peek.pm) perl(Encode.pm) perl(Exporter.pm) perl(HTML/Entities.pm) perl(IO/File.pm) perl(IO/Socket.pm) perl(LWP.pm) perl(PadWalker.pm) perl(Pod/Checker.pm) perl(Scalar/Util.pm) perl(Text/Iconv.pm) perl(Unicode/Map8.pm) perl(Unicode/String.pm) perl(XML/Parser.pm) perl(base.pm) perl(overload.pm) perl(threads.pm) perl(threads/shared.pm) unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
BuildRequires: rpm-build-java-osgi
Name:      eclipse-epic
Version:   0.6.44
Release:   alt1_3jpp7
Summary:   Perl Eclipse plug-in
Group:     Development/Java
License:   CPL
URL:       http://www.epic-ide.org/

# Fetched from https://github.com/jploski/epic-ide/tarball/testing
Source0:   jploski-epic-ide-273ac0e.tar.gz

# enable module starter and taint checking by default
Patch0:    %{name}-enable-module-starter.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    eclipse-pde >= 3.5
BuildRequires:    antlr
BuildRequires:    jdom
BuildRequires:    gnu-regexp
BuildRequires:    brazil
Requires:         jpackage-utils
Requires:         eclipse-platform >= 3.5
Requires:         antlr
Requires:         jdom
Requires:         gnu-regexp
Requires:         brazil
Requires:         perl
Requires:         perl(PadWalker.pm)
Requires:         perl(Module/Starter.pm)
Requires:         perl(Test/Simple.pm)
Requires:         perl(Perl/Tidy.pm)
Source44: import.info

%description
EPIC is an open source Perl IDE based on the Eclipse platform. Features 
supported are syntax highlighting, on-the-fly syntax check, content assist, 
perldoc support, source formatter, templating support, a regular expression 
view and a Perl debugger.

%prep
%setup -q -n jploski-epic-ide-273ac0e

# apply patches
%patch0 

# remove all bundled libs
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# build against fedora packaged libs
build-jar-repository -s -p org.epic.lib/lib jdom antlr gnu-regexp brazil

grep -lR jdom-1.1 *         | xargs sed --in-place "s/jdom-1.1/jdom/"
grep -lR antlr-2.7.5 *      | xargs sed --in-place "s/antlr-2.7.5/antlr/"
grep -lR gnu-regexp-1.1.4 * | xargs sed --in-place "s/gnu-regexp-1.1.4/gnu-regexp/"
grep -lR brazil_mini *      | xargs sed --in-place "s/brazil_mini/brazil/"

# put the source plugin together
for p in org.epic.perleditor \
         org.epic.regexp \
         org.epic.debug; do
  mkdir org.epic.source/src/$p
  pushd $p/src
  zip -r -q ../../org.epic.source/src/$p/src.zip *
  popd
done

%build
# parse grammar for grammar parser
pushd org.epic.perleditor/src/org/epic/core/parser/
for g in `find . -name "*.g"`; do
  antlr $g
done
popd

# build the main feature
eclipse-pdebuild -f org.epic.feature.main \
  -a "-DjavacTarget=1.4 -DjavacSource=1.4"

%install
installDir=%{buildroot}%{_datadir}/eclipse/dropins/epic
install -d -m 755 $installDir
unzip -q -d $installDir build/rpmBuild/org.epic.feature.main.zip

# need to recreate the symlinks to libraries that were setup in "prep"
# because for some reason the ant copy task doesn't preserve them
pushd $installDir/eclipse/plugins/org.epic.lib_*/lib
rm *.jar
build-jar-repository -s -p . jdom antlr gnu-regexp brazil
popd

# ensure source packages are correctly verisoned
pushd $installDir/eclipse/plugins
for p in org.epic.perleditor \
         org.epic.regexp \
         org.epic.debug; do
  PVERSION=_`ls -1 | grep $p | sed -r 's/.*_(.*)\.jar$/\1/'`
  mv org.epic.source_%{version}/src/$p org.epic.source_%{version}/src/$p$PVERSION
done
popd

%files
%doc org.epic.feature.main/license.html
%{_datadir}/eclipse/dropins/epic

%changelog
* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0.6.44-alt1_3jpp7
- new release

* Sun Mar 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.6.44-alt1_2jpp7
- fc update

* Mon Sep 17 2012 Igor Vlasenko <viy@altlinux.ru> 0.6.39-alt2_1jpp6
- fixed build

* Wed Sep 14 2011 Igor Vlasenko <viy@altlinux.ru> 0.6.39-alt1_1jpp6
- update to new release by jppimport

* Wed Jan 27 2010 Igor Vlasenko <viy@altlinux.ru> 0.6.35-alt1_2jpp6
- build for new eclipse version

* Fri Jan 02 2009 Igor Vlasenko <viy@altlinux.ru> 0.6.27-alt1_1jpp6
- new version

* Mon Jul 28 2008 Igor Vlasenko <viy@altlinux.ru> 0.6.24-alt1_2jpp6
- eclipse 3.3.2

