# BEGIN SourceDeps(oneline):
BuildRequires: perl(Statistics/Descriptive.pm) perl(Statistics/Distributions.pm) unzip
# END SourceDeps(oneline)
AutoReq: yes,noosgi
BuildRequires: rpm-build-java-osgi
BuildRequires: /proc
BuildRequires: jpackage-compat
# Copyright (c) 2000-2007, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

%global with_eclipse 1

%if 0%{?rhel}
%global with_eclipse 0
%endif

%global eclipse_base            %{_libdir}/eclipse
# Note:  this next section looks weird having an arch specified in a
# noarch specfile but the parts of the build
# All arches line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%global eclipse_arch    x86
%else
%global eclipse_arch   %{_arch}
%endif

Name:           icu4j
Version:        4.4.2.2
Release:        alt1_12jpp7
Epoch:          1
Summary:        International Components for Unicode for Java
License:        MIT and EPL 
URL:            http://site.icu-project.org/
Group:          Development/Java
#CAUTION
#to create a tarball use following procedure
#svn co http://source.icu-project.org/repos/icu/icu4j/tags/release-4-4-2-eclipse37-20110208/ icu4j-<version>
#tar caf icu4j-<version>.tar.xz icu4j-<version>/
Source0:        icu4j-4.4.2.2.tar.xz
Source1:        %{name}-4.4.2.pom
## CAUTION
## Please do not forget to update this Manifest to the latest one taken from the icu4j bundle from
## out/projects/ICU4J.com.ibm.icu/com.ibm.icu-com.ibm.icu.zip
## This is needed to unbreak cyclic dependencies between Eclipse and ICU4J
Source2:        icu4j-%{version}-MANIFEST.MF

Patch0:         %{name}-crosslink.patch
BuildRequires:  ant >= 1.7.0
# FIXME:  is this necessary or is it just adding strings in the hrefs in
# the docs?
BuildRequires:  java-javadoc
# This is to ensure we get OpenJDK and not GCJ
BuildRequires:  jpackage-utils >= 0:1.5
BuildRequires:  zip
Requires:       jpackage-utils
# This is to ensure we get OpenJDK and not GCJ
%if %{with_eclipse}
BuildRequires:  eclipse-pde >= 0:3.2.1
%global         debug_package %{nil}
%endif

BuildArch:      noarch
Source44: import.info
%define java_bin %_jvmdir/java/bin


%description
The International Components for Unicode (ICU) library provides robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and provides support for
supplementary characters (needed for GB 18030 repertoire support).

Java provides a very strong foundation for global programs, and IBM and the
ICU team played a key role in providing globalization technology into Sun's
Java. But because of its long release schedule, Java cannot always keep
up-to-date with evolving standards. The ICU team continues to extend Java's
Unicode and internationalization support, focusing on improving
performance, keeping current with the Unicode standard, and providing
richer APIs, while remaining as compatible as possible with the original
Java text and internationalization API design.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Java
Requires:       jpackage-utils
Requires:       java-javadoc
BuildArch: noarch

%description javadoc
Javadoc for %{name}.

%if %{with_eclipse}
%package eclipse
Summary:        Eclipse plugin for %{name}
Group:          Development/Java
Requires:       jpackage-utils

%description eclipse
Eclipse plugin support for %{name}.

%endif

%prep
%setup -q 
#%patch0 -p0

cp %{SOURCE1} .

%{__sed} -i 's/\r//' APIChangeReport.html
%{__sed} -i 's/\r//' readme.html

sed --in-place "s/ .*bootclasspath=.*//g" build.xml
sed --in-place "s/<date datetime=.*when=\"after\"\/>//" build.xml
sed --in-place "/javac1.3/d" build.xml
sed --in-place "s:/usr/lib:%{_datadir}:g" build.xml

%build
%ant -Dicu4j.javac.source=1.5 -Dicu4j.javac.target=1.5 -Dj2se.apidoc=%{_javadocdir}/java jar docs
%if %{with_eclipse}
pushd eclipse-build
  %ant -Dj2se.apidoc=%{_javadocdir}/java -Declipse.home=%{eclipse_base} \
    -Declipse.basews=gtk -Declipse.baseos=linux \
    -Declipse.pde.dir=%{eclipse_base}/dropins/sdk/plugins/`ls %{eclipse_base}/dropins/sdk/plugins/|grep org.eclipse.pde.build_`
popd
%endif
  
%install

# inject OSGi manifests
mkdir -p META-INF
cp -p %{SOURCE2} META-INF/MANIFEST.MF
touch META-INF/MANIFEST.MF
zip -u %{name}.jar META-INF/MANIFEST.MF

# jars
%__mkdir_p %{buildroot}%{_javadir}
%__cp -ap %{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
%__mkdir_p %{buildroot}%{_javadocdir}/%{name}
%__cp -pr doc/* %{buildroot}%{_javadocdir}/%{name}

%if %{with_eclipse}
# eclipse
install -d -m755 %{buildroot}%{_javadir}/icu4j-eclipse

unzip -qq -d %{buildroot}%{_javadir}/icu4j-eclipse eclipse-build/out/projects/ICU4J.com.ibm.icu/com.ibm.icu-com.ibm.icu.zip
%endif

# maven stuff
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
cp %{name}-4.4.2.pom $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom %{name}.jar

%files
%doc readme.html APIChangeReport.html
%{_javadir}/%{name}*.jar
%{_mavendepmapfragdir}/*
%{_mavenpomdir}/*.pom

%files javadoc
%doc %{_javadocdir}/*

%if %{with_eclipse}
%files eclipse
%dir %{_javadir}/icu4j-eclipse/
%dir %{_javadir}/icu4j-eclipse/features
%dir %{_javadir}/icu4j-eclipse/plugins
%{_javadir}/icu4j-eclipse/features/*
%{_javadir}/icu4j-eclipse/plugins/*
%doc readme.html
%endif

%changelog
* Wed Sep 05 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt1_12jpp7
- new version

* Wed Aug 29 2012 Igor Vlasenko <viy@altlinux.ru> 1:4.4.2.2-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

