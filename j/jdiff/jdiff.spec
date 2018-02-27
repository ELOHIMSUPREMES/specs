Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-java
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat

Name:          jdiff
Version:       1.1.1
Release:       alt2_5jpp7
Summary:       An HTML Report of API Differences
Group:         Development/Java
License:       GPL+ and LGPLv2+
URL:           http://javadiff.sourceforge.net/
# cvs -d:pserver:anonymous@javadiff.cvs.sourceforge.net:/cvsroot/javadiff login
# cvs -z3 -d:pserver:anonymous@javadiff.cvs.sourceforge.net:/cvsroot/javadiff export -rHEAD jdiff
# removing unneeded files
# find jdiff -name .cvsignore -delete
# find jdiff -name "*.jar" -delete
# find jdiff -name "*.class" -delete
# tar czf jdiff-1.1.1-clean-src-cvs.tar.gz jdiff
Source0:       jdiff-1.1.1-clean-src-cvs.tar.gz
Source1:       jdiff-pom-template.xml
Source2:       jdiff-script

BuildRequires: jpackage-utils

BuildRequires: ant
BuildRequires: junit
BuildRequires: xerces-j2

Requires:      ant
Requires:      xerces-j2

Requires:      jpackage-utils
BuildArch:     noarch
Source44: import.info

%description
JDiff is a Javadoc doclet which generates an HTML 
report of all the packages, classes, constructors, 
methods, and fields which have been removed, added 
or changed in any way, including their documentation, 
when two APIs are compared. This is very useful for 
describing exactly what has changed between two 
releases of a product. Only the API (Application 
Programming Interface) of each version is compared. 
It does not compare what the source code does when 
executed. 

%package javadoc
Group:         Development/Java
Summary:       Javadoc for %{name}
Requires:      jpackage-utils
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n jdiff
perl -pi -e 's/\r$//g' doc/CHANGES.txt doc/KNOWN_LIMITATIONS.txt doc/TODO doc/dev_notes.txt

perl -pi -e 's/\r$//g' LICENSE.txt README.txt

ln -sf $(build-classpath xerces-j2) lib/xerces.jar

# fix non ASCII chars
native2ascii -encoding UTF8 test/old/ChangedPackageDoc2/ChangedMethod.java test/old/ChangedPackageDoc2/ChangedMethod.java
native2ascii -encoding UTF8 test/new/ChangedPackageDoc2/ChangedMethod.java test/new/ChangedPackageDoc2/ChangedMethod.java

%build
export CLASSPATH=$(build-classpath junit):`pwd`/build/lib/jdiff.jar:`pwd`/build/lib/antjdiff.jar
%{ant} -Dbuild.sysclasspath=only release

%javadoc -classpath `pwd`/build/lib/jdiff.jar:`pwd`/build/lib/antjdiff.jar:$(build-classpath xerces-j2 ant.jar ../jvm/java/lib/tools) \
-d apidocs -sourcepath src -subpackages jdiff

%install

mkdir -p %{buildroot}%{_javadir}
install -pm 644 build/lib/ant%{name}.jar %{buildroot}%{_javadir}/ant%{name}.jar
install -pm 644 build/lib/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_mavenpomdir}
install -pm 644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
sed -i "s|@version@|%{version}|" %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr apidocs/* %{buildroot}%{_javadocdir}/%{name}

mkdir -p %{buildroot}%{_bindir}
install -pm 755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}

mkdir -p $RPM_BUILD_ROOT`dirname /etc/java/%{name}.conf`
touch $RPM_BUILD_ROOT/etc/java/%{name}.conf

%files
%{_bindir}/%{name}
%{_javadir}/*%{name}.jar
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}/%{name}
%doc LICENSE.txt README.txt doc/jdiff.html doc/CHANGES.txt doc/KNOWN_LIMITATIONS.txt doc/TODO doc/dev_notes.txt
%config(noreplace,missingok) /etc/java/%{name}.conf

%files javadoc
%{_javadocdir}/%{name}
%doc LICENSE.txt

%changelog
* Mon Sep 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_5jpp7
- new release

* Mon Jul 28 2014 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_4jpp7
- new release

* Fri Mar 22 2013 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_3jpp7
- fc update

* Tue Mar 20 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt2_1jpp6
- fixed build with maven3

* Mon Jan 16 2012 Igor Vlasenko <viy@altlinux.ru> 0:1.1.1-alt1_1jpp6
- new jpp relase

* Sun Mar 29 2009 Igor Vlasenko <viy@altlinux.ru> 0:1.1.0-alt1_1jpp5
- fixed repocop warnings

* Mon Jun 04 2007 Igor Vlasenko <viy@altlinux.ru> 0:1.0.10-alt1_2jpp1.7
- converted from JPackage by jppimport script

