import rest_framework_filters as filters
from mrbelvedereci.build.models import Build
from mrbelvedereci.build.models import BuildFlow
from mrbelvedereci.build.models import Rebuild
from mrbelvedereci.cumulusci.filters import OrgRelatedFilter
from mrbelvedereci.cumulusci.filters import ScratchOrgInstanceRelatedFilter
from mrbelvedereci.cumulusci.models import Org
from mrbelvedereci.cumulusci.models import ScratchOrgInstance
from mrbelvedereci.plan.filters import PlanRelatedFilter
from mrbelvedereci.plan.models import Plan
from mrbelvedereci.repository.filters import BranchRelatedFilter
from mrbelvedereci.repository.filters import RepositoryRelatedFilter
from mrbelvedereci.repository.models import Branch
from mrbelvedereci.repository.models import Repository

class BuildRelatedFilter(filters.FilterSet):
    branch = filters.RelatedFilter(
        BranchRelatedFilter,
        name='branch',
        queryset=Branch.objects.all()
    )
    org = filters.RelatedFilter(
        OrgRelatedFilter,
        name='org',
        queryset=Org.objects.all()
    )
    plan = filters.RelatedFilter(
        PlanRelatedFilter,
        name='plan',
        queryset=Plan.objects.all()
    )
    repo = filters.RelatedFilter(
        RepositoryRelatedFilter,
        name='repo',
        queryset=Repository.objects.all()
    )

    class Meta:
        model = Build
        fields = {
            'commit': ['exact'],
            'status': ['exact'],
            'time_queue': ['gt','lt'],
            'time_start': ['gt','lt'],
            'time_end': ['gt','lt'],
        }

class BuildFilter(BuildRelatedFilter):
    pass

class RebuildRelatedFilter(filters.FilterSet):
    build = filters.RelatedFilter(
        BuildRelatedFilter,
        name='build',
        queryset=Build.objects.all()
    )
    class Meta:
        model = Rebuild
        fields = {
            'status': ['exact'],
            'time_queue': ['gt','lt'],
            'time_start': ['gt','lt'],
            'time_end': ['gt','lt'],
        }

class RebuildFilter(RebuildRelatedFilter):
    pass


class BuildFlowRelatedFilter(filters.FilterSet):
    build = filters.RelatedFilter(
        BuildRelatedFilter,
        name='build',
        queryset=Build.objects.all()
    )
    rebuild = filters.RelatedFilter(
        RebuildRelatedFilter,
        name='build',
        queryset=Rebuild.objects.all()
    )

    class Meta:
        model = BuildFlow
        fields = {
            'status': ['exact'],
            'time_queue': ['gt','lt'],
            'time_start': ['gt','lt'],
            'time_end': ['gt','lt'],
        }
   
class BuildFlowFilter(BuildFlowRelatedFilter):
    pass 