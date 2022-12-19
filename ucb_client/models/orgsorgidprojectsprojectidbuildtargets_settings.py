# coding: utf-8

"""
    Unity Cloud Build

    This API is intended to be used in conjunction with the Unity Cloud Build service. A tool for building your Unity projects in the Cloud.  See https://developer.cloud.unity3d.com for more information.  ## Making requests This website is built to allow requests to be made against the API. If you are currently logged into Cloud Build you should be able to make requests without entering an API key.   You can find your API key in the Unity Cloud Services portal by clicking on 'Cloud Build Preferences' in the sidebar. Copy the API Key and paste it into the upper left corner of this website. It will be used in all subsequent requests.  ## Clients The Unity Cloud Build API is based upon Swagger. Client libraries to integrate with your projects can easily be generated with the [Swagger Code Generator](https://github.com/swagger-api/swagger-codegen).  The JSON schema required to generate a client for this API version is located here:  ``` [API_URL][BASE_PATH]/api.json ```  ## Authorization The Unity Cloud Build API requires an access token from your Unity Cloud Build account, which can be found by selecting **Settings** under **DevOps > Cloud Build** at https://dashboard.unity3d.com/cloud-build  To authenticate requests, include a Basic Authentication header with your API key as the value. e.g.  ``` Authorization: Basic [YOUR API KEY] ```  ## Pagination Paged results will take two parameters. A page number that is calculated based upon the per_page amount. For instance if there are 40 results and you specify page 2 with per_page set to 10 you will receive records 11-20.  Paged results will also return a Content-Range header. For the example above the content range header would look like this:  ``` Content-Range: items 11-20/40 ```  ## Versioning The API version is indicated in the request URL. Upgrading to a newer API version can be done by changing the path.  The API will receive a new version in the following cases:    * removal of a path or request type   * addition of a required field   * removal of a required field  The following changes are considered backwards compatible and will not trigger a new API version:    * addition of an endpoint or request type   * addition of an optional field   * removal of an optional field   * changes to the format of ids  ## Identifiers It should not be assumed that any of the identifiers used in paths will be a perfect match for your user-entered information. If you see unexpected 403s or 404s from API calls then check your identifiers match the ones used by the API. In particular, `projectId` does NOT typically change when the project is renamed and in fact may not be a direct match for the project name even at initial creation time.  To avoid confusion we recommend that instead of using the human-readable autogenerated orgId and projectId available from the API you should instead use:   * org foreign key for `orgId` (available from project APIs as `orgFk` and org APIs as `coreForeignKey`)   * `guid` for `projectId`  All links generated by the API and the Dashboard should follow this format already, making it easy to figure out the correct parameters by making a comparison.  ## Rate Limiting Requests against the Cloud Build API are limited to a rate of 100 per minute. To preserve the quality of service throughout Cloud Build, additional rate limits may apply to some actions. For example, polling aggressively instead of using webhooks or making API calls with a high concurrency may result in rate limiting.  It is not intended for these rate limits to interfere with any legitimate use of the API. Please contact support at <cloudbuild@unity3d.com> if your use is affected by this rate limit.  You can check the returned HTTP headers for any API request to see your current rate limit status.   * __X-RateLimit-Limit:__ maximum number of requests per minute   * __X-RateLimit-Remaining:__ remaining number of requests in the current window   * __X-RateLimit-Reset:__ time at which the current window will reset (UTC epoch seconds)  Once you go over the rate limit you will receive an error response: ``` HTTP Status: 429 {   \"error\": \"Rate limit exceeded, retry in XX seconds\" } ```   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ucb_client.configuration import Configuration


class OrgsorgidprojectsprojectidbuildtargetsSettings(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'auto_build': 'bool',
        'unity_version': 'str',
        'auto_detect_unity_version': 'bool',
        'fallback_patch_version': 'bool',
        'executablename': 'str',
        'scm': 'OrgsorgidprojectsprojectidbuildtargetsSettingsScm',
        'platform': 'OrgsorgidprojectsprojectidbuildtargetsSettingsPlatform',
        'build_schedule': 'OrgsorgidprojectsprojectidbuildtargetsSettingsBuildSchedule',
        'auto_build_cancellation': 'bool',
        'operating_system_selected': 'str',
        'ruby_version': 'str',
        'advanced': 'OrgsorgidprojectsprojectidbuildtargetsSettingsAdvanced'
    }

    attribute_map = {
        'auto_build': 'autoBuild',
        'unity_version': 'unityVersion',
        'auto_detect_unity_version': 'autoDetectUnityVersion',
        'fallback_patch_version': 'fallbackPatchVersion',
        'executablename': 'executablename',
        'scm': 'scm',
        'platform': 'platform',
        'build_schedule': 'buildSchedule',
        'auto_build_cancellation': 'autoBuildCancellation',
        'operating_system_selected': 'operatingSystemSelected',
        'ruby_version': 'rubyVersion',
        'advanced': 'advanced'
    }

    def __init__(self, auto_build=None, unity_version=None, auto_detect_unity_version=None, fallback_patch_version=None, executablename=None, scm=None, platform=None, build_schedule=None, auto_build_cancellation=False, operating_system_selected=None, ruby_version=None, advanced=None, _configuration=None):  # noqa: E501
        """OrgsorgidprojectsprojectidbuildtargetsSettings - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._auto_build = None
        self._unity_version = None
        self._auto_detect_unity_version = None
        self._fallback_patch_version = None
        self._executablename = None
        self._scm = None
        self._platform = None
        self._build_schedule = None
        self._auto_build_cancellation = None
        self._operating_system_selected = None
        self._ruby_version = None
        self._advanced = None
        self.discriminator = None

        if auto_build is not None:
            self.auto_build = auto_build
        if unity_version is not None:
            self.unity_version = unity_version
        if auto_detect_unity_version is not None:
            self.auto_detect_unity_version = auto_detect_unity_version
        if fallback_patch_version is not None:
            self.fallback_patch_version = fallback_patch_version
        if executablename is not None:
            self.executablename = executablename
        if scm is not None:
            self.scm = scm
        if platform is not None:
            self.platform = platform
        if build_schedule is not None:
            self.build_schedule = build_schedule
        if auto_build_cancellation is not None:
            self.auto_build_cancellation = auto_build_cancellation
        if operating_system_selected is not None:
            self.operating_system_selected = operating_system_selected
        if ruby_version is not None:
            self.ruby_version = ruby_version
        if advanced is not None:
            self.advanced = advanced

    @property
    def auto_build(self):
        """Gets the auto_build of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501

        start builds automatically when your repo is updated  # noqa: E501

        :return: The auto_build of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_build

    @auto_build.setter
    def auto_build(self, auto_build):
        """Sets the auto_build of this OrgsorgidprojectsprojectidbuildtargetsSettings.

        start builds automatically when your repo is updated  # noqa: E501

        :param auto_build: The auto_build of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: bool
        """

        self._auto_build = auto_build

    @property
    def unity_version(self):
        """Gets the unity_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501

        'latest' or a unity dot version with underscores (ex. '4_6_5')  # noqa: E501

        :return: The unity_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: str
        """
        return self._unity_version

    @unity_version.setter
    def unity_version(self, unity_version):
        """Sets the unity_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.

        'latest' or a unity dot version with underscores (ex. '4_6_5')  # noqa: E501

        :param unity_version: The unity_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: str
        """

        self._unity_version = unity_version

    @property
    def auto_detect_unity_version(self):
        """Gets the auto_detect_unity_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501

        attempt to automatically detect which unity version to use, fallback to specified unityVersion if unable to.  # noqa: E501

        :return: The auto_detect_unity_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_detect_unity_version

    @auto_detect_unity_version.setter
    def auto_detect_unity_version(self, auto_detect_unity_version):
        """Sets the auto_detect_unity_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.

        attempt to automatically detect which unity version to use, fallback to specified unityVersion if unable to.  # noqa: E501

        :param auto_detect_unity_version: The auto_detect_unity_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: bool
        """

        self._auto_detect_unity_version = auto_detect_unity_version

    @property
    def fallback_patch_version(self):
        """Gets the fallback_patch_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501

        attempt to get a similar unity patch version to use, applies to unavailable auto-detected Unity versions only.  # noqa: E501

        :return: The fallback_patch_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._fallback_patch_version

    @fallback_patch_version.setter
    def fallback_patch_version(self, fallback_patch_version):
        """Sets the fallback_patch_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.

        attempt to get a similar unity patch version to use, applies to unavailable auto-detected Unity versions only.  # noqa: E501

        :param fallback_patch_version: The fallback_patch_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: bool
        """

        self._fallback_patch_version = fallback_patch_version

    @property
    def executablename(self):
        """Gets the executablename of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501


        :return: The executablename of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: str
        """
        return self._executablename

    @executablename.setter
    def executablename(self, executablename):
        """Sets the executablename of this OrgsorgidprojectsprojectidbuildtargetsSettings.


        :param executablename: The executablename of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: str
        """

        self._executablename = executablename

    @property
    def scm(self):
        """Gets the scm of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501


        :return: The scm of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsScm
        """
        return self._scm

    @scm.setter
    def scm(self, scm):
        """Sets the scm of this OrgsorgidprojectsprojectidbuildtargetsSettings.


        :param scm: The scm of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsScm
        """

        self._scm = scm

    @property
    def platform(self):
        """Gets the platform of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501


        :return: The platform of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this OrgsorgidprojectsprojectidbuildtargetsSettings.


        :param platform: The platform of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsPlatform
        """

        self._platform = platform

    @property
    def build_schedule(self):
        """Gets the build_schedule of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501


        :return: The build_schedule of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsBuildSchedule
        """
        return self._build_schedule

    @build_schedule.setter
    def build_schedule(self, build_schedule):
        """Sets the build_schedule of this OrgsorgidprojectsprojectidbuildtargetsSettings.


        :param build_schedule: The build_schedule of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsBuildSchedule
        """

        self._build_schedule = build_schedule

    @property
    def auto_build_cancellation(self):
        """Gets the auto_build_cancellation of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501


        :return: The auto_build_cancellation of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: bool
        """
        return self._auto_build_cancellation

    @auto_build_cancellation.setter
    def auto_build_cancellation(self, auto_build_cancellation):
        """Sets the auto_build_cancellation of this OrgsorgidprojectsprojectidbuildtargetsSettings.


        :param auto_build_cancellation: The auto_build_cancellation of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: bool
        """

        self._auto_build_cancellation = auto_build_cancellation

    @property
    def operating_system_selected(self):
        """Gets the operating_system_selected of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501


        :return: The operating_system_selected of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: str
        """
        return self._operating_system_selected

    @operating_system_selected.setter
    def operating_system_selected(self, operating_system_selected):
        """Sets the operating_system_selected of this OrgsorgidprojectsprojectidbuildtargetsSettings.


        :param operating_system_selected: The operating_system_selected of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["mac", "windows", "automatic"]  # noqa: E501
        if (self._configuration.client_side_validation and
                operating_system_selected not in allowed_values):
            raise ValueError(
                "Invalid value for `operating_system_selected` ({0}), must be one of {1}"  # noqa: E501
                .format(operating_system_selected, allowed_values)
            )

        self._operating_system_selected = operating_system_selected

    @property
    def ruby_version(self):
        """Gets the ruby_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501


        :return: The ruby_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: str
        """
        return self._ruby_version

    @ruby_version.setter
    def ruby_version(self, ruby_version):
        """Sets the ruby_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.


        :param ruby_version: The ruby_version of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: str
        """

        self._ruby_version = ruby_version

    @property
    def advanced(self):
        """Gets the advanced of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501


        :return: The advanced of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :rtype: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvanced
        """
        return self._advanced

    @advanced.setter
    def advanced(self, advanced):
        """Sets the advanced of this OrgsorgidprojectsprojectidbuildtargetsSettings.


        :param advanced: The advanced of this OrgsorgidprojectsprojectidbuildtargetsSettings.  # noqa: E501
        :type: OrgsorgidprojectsprojectidbuildtargetsSettingsAdvanced
        """

        self._advanced = advanced

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(OrgsorgidprojectsprojectidbuildtargetsSettings, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrgsorgidprojectsprojectidbuildtargetsSettings):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OrgsorgidprojectsprojectidbuildtargetsSettings):
            return True

        return self.to_dict() != other.to_dict()
