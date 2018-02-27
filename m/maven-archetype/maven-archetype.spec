Epoch: 0
# BEGIN SourceDeps(oneline):
BuildRequires: unzip maven-local
# END SourceDeps(oneline)
BuildRequires: /proc
BuildRequires: jpackage-compat
Name:           maven-archetype
Version:        2.2
Release:        alt1_1jpp7
Summary:        Maven project templating toolkit

Group:          Development/Java
License:        ASL 2.0
URL:            https://maven.apache.org/archetype/
Source0:        http://repo.maven.apache.org/maven2/org/apache/maven/archetype/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch1:         0002-Use-generics.patch
Patch2:         0003-Add-Maven-3-compatibility.patch
Patch3:         %{name}-fix-jetty-namespace.patch

BuildArch:      noarch

BuildRequires:  jpackage-utils
# we added test dep skipping there
BuildRequires:  maven-war-plugin
BuildRequires:  maven-dependency-plugin
BuildRequires:  maven-plugin-bundle
BuildRequires:  maven-script-interpreter
BuildRequires:  jchardet
BuildRequires:  plexus-containers-component-metadata
BuildRequires:  xmvn
Source44: import.info
Provides: maven-archetype2 = %version
Obsoletes: maven-archetype2 < %version


%description
Archetype is a Maven project templating toolkit. An archetype is
defined as an original pattern or model from which all other things of
the same kind are made. The names fits as we are trying to provide a
system that provides a consistent means of generating Maven
projects. Archetype will help authors create Maven project templates
for users, and provides users with the means to generate parameterized
versions of those project templates.

Using archetypes provides a great way to enable developers quickly in
a way consistent with best practices employed by your project or
organization. Within the Maven project we use archetypes to try and
get our users up and running as quickly as possible by providing a
sample project that demonstrates many of the features of Maven while
introducing new users to the best practices employed by Maven. In a
matter of seconds a new user can have a working Maven project to use
as a jumping board for investigating more of the features in Maven. We
have also tried to make the Archetype mechanism additive and by that
we mean allowing portions of a project to be captured in an archetype
so that pieces or aspects of a project can be added to existing
projects. A good example of this is the Maven site archetype. If, for
example, you have used the quick start archetype to generate a working
project you can then quickly create a site for that project by using
the site archetype within that existing project. You can do anything
like this with archetypes.

You may want to standardize J2EE development within your organization
so you may want to provide archetypes for EJBs, or WARs, or for your
web services. Once these archetypes are created and deployed in your
organization's repository they are available for use by all developers
within your organization.


%package javadoc
Summary:        API documentation for %{name}
Group:          Development/Java
BuildArch: noarch

%description    javadoc
%{summary}.

%package catalog
Summary:        Maven Archetype Catalog model
Group:          Development/Java

%description catalog
%{summary}.

%package descriptor
Summary:        Maven Archetype Descriptor model
Group:          Development/Java

%description descriptor
%{summary}.

%package registry
Summary:        Maven Archetype Registry model
Group:          Development/Java

%description registry
%{summary}.

%package common
Summary:        Maven Archetype common classes
Group:          Development/Java

%description common
%{summary}.

%package packaging
Summary:        Maven Archetype packaging configuration for archetypes
Group:          Development/Java

%description packaging
%{summary}.

%package -n %{name}-plugin
Summary:        Maven Plugin for using archetypes
Group:          Development/Java

%description -n %{name}-plugin
%{summary}.

%prep
%setup -q

%patch1 -p1
%patch2 -p1
%patch3

# Add OSGI info to catalog and descriptor jars
pushd archetype-models/archetype-catalog
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.catalog.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd
pushd archetype-models/archetype-descriptor
    %pom_xpath_remove "pom:project/pom:packaging"
    %pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
    %pom_xpath_inject "pom:build/pom:plugins" "
      <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <extensions>true</extensions>
        <configuration>
          <instructions>
            <_nouses>true</_nouses>
            <Export-Package>org.apache.maven.archetype.metadata.*</Export-Package>
          </instructions>
        </configuration>
      </plugin>"
popd


# groovy is not really needed
%pom_remove_dep org.codehaus.groovy:groovy maven-archetype-plugin/pom.xml

%pom_disable_module archetype-testing
%pom_remove_plugin org.apache.maven.plugins:maven-antrun-plugin archetype-common/pom.xml


%build
%mvn_package :archetype-models maven-archetype
# we don't have cargo so skip tests for now
%mvn_build -s -f

%install
%mvn_install


%files -f .mfiles-maven-archetype
%doc LICENSE NOTICE

%files catalog -f .mfiles-archetype-catalog

%files descriptor -f .mfiles-archetype-descriptor

%files registry -f .mfiles-archetype-registry

%files common -f .mfiles-archetype-common

%files packaging -f .mfiles-archetype-packaging

%files -n %{name}-plugin -f .mfiles-maven-archetype-plugin

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Mon Aug 25 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.2-alt1_1jpp7
- new release

* Fri Aug 08 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt5_7jpp7
- rebuild with maven-local

* Fri Jul 18 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt4_7jpp7
- fixed build

* Mon Jul 14 2014 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt3_7jpp7
- NMU rebuild to move poms and fragments

* Tue Sep 11 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt2_7jpp7
- fixed build

* Fri Aug 24 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.1-alt1_7jpp7
- new version

* Fri Jun 22 2012 Igor Vlasenko <viy@altlinux.ru> 0:2.0-alt0.1jpp
- bootstrap pack of jars created with jppbootstrap script
- temporary package to satisfy circular dependencies

