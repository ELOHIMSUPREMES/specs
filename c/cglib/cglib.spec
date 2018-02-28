Epoch: 0
Group: Development/Java
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
%filter_from_requires /^java-headless/d
BuildRequires: /proc
BuildRequires: jpackage-generic-compat
Name:           cglib
Version:        3.1
Release:        alt1_7jpp8
Summary:        Code Generation Library for Java
License:        ASL 2.0 and BSD
Url:            http://cglib.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-src-%{version}.jar
Source1:        http://mirrors.ibiblio.org/pub/mirrors/maven2/%{name}/%{name}/%{version}/%{name}-%{version}.pom
Source2:        bnd.properties

Requires: objectweb-asm

BuildRequires:  ant
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  objectweb-asm
BuildRequires:  unzip
BuildRequires:  aqute-bnd
BuildArch:      noarch
Source44: import.info

%description
cglib is a powerful, high performance and quality code generation library
for Java. It is used to extend Java classes and implements interfaces
at runtime.

%package javadoc
Group: Development/Java
Summary:        Javadoc for %{name}
BuildArch: noarch

%description javadoc
Documentation for the cglib code generation library.

%prep
%setup -q -c %{name}-%{version}
cp -p %{SOURCE1} pom.xml
rm lib/*.jar
# Remove the repackaging step that includes other jars into the final thing
sed -i "/<taskdef name=.jarjar/,/<.jarjar>/d" build.xml

%pom_xpath_remove "pom:dependency[pom:artifactId = 'asm-util']/pom:optional"

%build
export OPT_JAR_LIST=objectweb-asm
ant jar javadoc
# Convert to OSGi bundle
bnd wrap --output dist/%{name}-%{version}.bar --properties %{SOURCE2} \
         --version %{version} dist/%{name}-%{version}.jar

%install
install -d -m 755 %{buildroot}%{_javadir}
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_mavenpomdir}
# yes, this is really *.bar - aqute bnd created it
install -p -m 644 dist/%{name}-%{version}.bar %{buildroot}%{_javadir}/%{name}.jar
install -p -m 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap -a net.sf.cglib:cglib,cglib:cglib-full,cglib:cglib-nodep,org.sonatype.sisu.inject:cglib

cp -rp docs/* %{buildroot}%{_javadocdir}/%{name}

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc
%doc LICENSE NOTICE
%{_javadocdir}/%{name}

%changelog
* Fri Feb 05 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt1_7jpp8
- java 8 mass update

* Mon Feb 01 2016 Igor Vlasenko <viy@altlinux.ru> 0:3.1-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_17jpp7
- new release

* Tue Mar 12 2013 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_15jpp7
- fc update

* Thu Mar 08 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt2_4jpp6
- added net.sf.cglib group id

* Sat Oct 23 2010 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_4jpp6
- added pom

* Mon Jan 05 2009 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_4jpp5
- fixed docdir ownership

* Sat Sep 06 2008 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_3jpp5
- converted from JPackage by jppimport script

* Fri Jun 08 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt5_2jpp1.7
- converted from JPackage by jppimport script

* Wed May 30 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt4_2jpp1.7
- fixed provides to avoid unmets on cglib

* Fri May 25 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt3_2jpp1.7
- imported with jppimport script; note: bootstrapped version

* Thu May 24 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt2_2jpp1.7
- fixed cglib provides

* Sat May 19 2007 Igor Vlasenko <viy@altlinux.ru> 0:2.1.3-alt1_2jpp1.7
- imported with jppimport script; note: bootstrapped version

