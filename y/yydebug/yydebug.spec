Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires: rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:     yydebug
Version:  1.1.0
Release:  alt1_20jpp8
Summary:  Supports tracing and animation for a Java-based parser generated by jay
License:  BSD
URL:      http://www.cs.rit.edu/~ats/projects/lp/doc/jay/yydebug/package-summary.html
Source0:  http://www.cs.rit.edu/~ats/projects/lp/doc/jay/yydebug/doc-files/src.jar
Source1:  http://repo1.maven.org/maven2/org/jruby/jay-yydebug/1.0/jay-yydebug-1.0.pom

BuildRequires: maven-local
BuildRequires: sonatype-oss-parent

BuildArch:      noarch
Source44: import.info

%description
jay/yydebug supports tracing and animation for a Java-based parser generated 
by jay. An implementation of yyDebug is passed as an additional argument to 
yyparse() to trace a Java-based parser generated by jay with option -t set.
yyDebugAdapter produces one-line messages, by default to standard output. 
The messages are designed to be filtered by a program such as grep. yyAnim 
provides an animation of the parsing process

%package javadoc
Group: Development/Java
Summary:        Javadocs for %{name}
BuildArch: noarch

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jay-yydebug -c %{name}-%{version}

find ./ -name '*.jar' -exec rm -f '{}' \; 
find ./ -name '*.class' -exec rm -f '{}' \; 

cp %{SOURCE1} pom.xml

%mvn_file : %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc jay/yydebug/package.html

%files javadoc -f .mfiles-javadoc


%changelog
* Sun May 26 2019 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_20jpp8
- new version

* Mon Apr 16 2018 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_18jpp8
- java update

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_17jpp8
- fixed build

* Tue Nov 22 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_14jpp8
- new fc release

* Tue Feb 02 2016 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_13jpp8
- new version

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_10jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_9jpp7
- new release

* Mon Oct 01 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_8jpp7
- new fc release

* Sat Apr 07 2012 Igor Vlasenko <viy@altlinux.ru> 1.1.0-alt1_7jpp7
- new version

