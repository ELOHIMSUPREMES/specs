Group: Development/Java
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:          osgi-resource-locator
Version:       1.0.1
Release:       alt1_3jpp7
Summary:       OSGi resource locator bundle
License:       CDDL or GPLv2 with exceptions
Url:           http://hk2.java.net/
# svn export https://svn.java.net/svn/hk2~svn/tags/osgi-resource-locator-1.0.1
# tar czf osgi-resource-locator-1.0.1-src-svn.tar.gz osgi-resource-locator-1.0.1
Source0:       %{name}-%{version}-src-svn.tar.gz
# wget -O glassfish-LICENSE.txt https://svn.java.net/svn/glassfish~svn/tags/legal-1.1/src/main/resources/META-INF/LICENSE.txt
# glassfish-master-pom package don't include the license file
Source1:       glassfish-LICENSE.txt


BuildRequires: felix-osgi-compendium
BuildRequires: felix-osgi-core
BuildRequires: glassfish-master-pom

BuildRequires: maven-local
BuildRequires: maven-plugin-bundle

BuildArch:     noarch
Source44: import.info

%description
OSGi resource locator bundle - used by various API providers that
rely on META-INF/services mechanism to locate providers.

%package javadoc
Group: Development/Java
Summary:       Javadoc for %{name}
BuildArch: noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q
cp -p %{SOURCE1} LICENSE.txt
sed -i 's/\r//' LICENSE.txt

%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId ='maven-jar-plugin']" "<version>2.4</version>"

%build

%mvn_file :%{name} %{name}
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.1-alt1_3jpp7
- new release

