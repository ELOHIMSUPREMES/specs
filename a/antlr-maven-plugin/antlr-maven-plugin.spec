# BEGIN SourceDeps(oneline):
BuildRequires: unzip
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:			antlr-maven-plugin
Version:		2.2
Release:		alt3_12jpp7
Summary:		Maven plugin that generates files based on grammar file(s)
License:		ASL 2.0
URL:			http://mojo.codehaus.org/antlr-maven-plugin/
Group:			Development/Java

Source0:		http://repo1.maven.org/maven2/org/codehaus/mojo/%{name}/%{version}/%{name}-%{version}-source-release.zip

# Modern modello expects to see <models></models>, even if there is only one.
Patch0:			maven-antlr-plugin-2.2-modello-issue.patch
# siteRenderer.createSink doesn't exist anymore
Patch2:			maven-antlr-plugin-2.1-sinkfix.patch
# Fix grammar processing bug (bz 1020312)
Patch3:			0001-MANTLR-34-Fix-NPE-when-building-Jenkins.patch

BuildArch:		noarch

BuildRequires:		jpackage-utils
BuildRequires:		antlr
BuildRequires:		maven-local
BuildRequires:		maven-plugin-bundle
BuildRequires:		maven-plugin-cobertura
BuildRequires:		apache-commons-exec
BuildRequires:		modello

Provides:		maven2-plugin-antlr = %{version}-%{release}
Obsoletes:		maven2-plugin-antlr <= 2.0.8
Source44: import.info

Provides: mojo-maven2-plugin-antlr = %version
Obsoletes: mojo-maven2-plugin-antlr = 17


%description
The Antlr Plugin has two goals:
- antlr:generate Generates file(s) to a target directory based on grammar
  file(s).
- antlr:html Generates Antlr report for grammar file(s).

%package javadoc
Summary:		Javadocs for %{name}
Group:			Development/Java
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q
%patch0 -p1 -b .modello
%patch2 -p1 -b .sink
%patch3 -p1 -b .fixnpe

# reporting eventually pulls in another antlr and we'd break with weird errors
%pom_xpath_inject "pom:dependency[pom:artifactId[text()='maven-reporting-impl']]/pom:exclusions" "
        <exclusion>
            <groupId>antlr</groupId>
            <artifactId>antlr</artifactId>
        </exclusion>"

# remove all binary bits
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

%mvn_file : %{name}

%build
%mvn_build -- -Dmaven.test.skip=true

%install
%mvn_install

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_12jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_9jpp7
- new release

* Thu Jul 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt3_6jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 2.2-alt2_6jpp7
- NMU rebuild to move poms and fragments

* Mon Aug 27 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_6jpp7
- new release

* Sat Mar 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.2-alt1_5jpp7
- new version

