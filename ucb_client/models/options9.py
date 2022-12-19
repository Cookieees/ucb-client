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


class Options9(object):
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
        'clean': 'bool',
        'delay': 'float',
        'commit': 'str',
        'headless': 'bool',
        'label': 'str',
        'platform': 'str'
    }

    attribute_map = {
        'clean': 'clean',
        'delay': 'delay',
        'commit': 'commit',
        'headless': 'headless',
        'label': 'label',
        'platform': 'platform'
    }

    def __init__(self, clean=None, delay=None, commit=None, headless=None, label=None, platform=None, _configuration=None):  # noqa: E501
        """Options9 - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._clean = None
        self._delay = None
        self._commit = None
        self._headless = None
        self._label = None
        self._platform = None
        self.discriminator = None

        if clean is not None:
            self.clean = clean
        if delay is not None:
            self.delay = delay
        if commit is not None:
            self.commit = commit
        if headless is not None:
            self.headless = headless
        if label is not None:
            self.label = label
        if platform is not None:
            self.platform = platform

    @property
    def clean(self):
        """Gets the clean of this Options9.  # noqa: E501


        :return: The clean of this Options9.  # noqa: E501
        :rtype: bool
        """
        return self._clean

    @clean.setter
    def clean(self, clean):
        """Sets the clean of this Options9.


        :param clean: The clean of this Options9.  # noqa: E501
        :type: bool
        """

        self._clean = clean

    @property
    def delay(self):
        """Gets the delay of this Options9.  # noqa: E501

        Delay to start build, in milliseconds  # noqa: E501

        :return: The delay of this Options9.  # noqa: E501
        :rtype: float
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this Options9.

        Delay to start build, in milliseconds  # noqa: E501

        :param delay: The delay of this Options9.  # noqa: E501
        :type: float
        """

        self._delay = delay

    @property
    def commit(self):
        """Gets the commit of this Options9.  # noqa: E501


        :return: The commit of this Options9.  # noqa: E501
        :rtype: str
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        """Sets the commit of this Options9.


        :param commit: The commit of this Options9.  # noqa: E501
        :type: str
        """

        self._commit = commit

    @property
    def headless(self):
        """Gets the headless of this Options9.  # noqa: E501

        Only valid for local builds   # noqa: E501

        :return: The headless of this Options9.  # noqa: E501
        :rtype: bool
        """
        return self._headless

    @headless.setter
    def headless(self, headless):
        """Sets the headless of this Options9.

        Only valid for local builds   # noqa: E501

        :param headless: The headless of this Options9.  # noqa: E501
        :type: bool
        """

        self._headless = headless

    @property
    def label(self):
        """Gets the label of this Options9.  # noqa: E501

        Only valid for local builds   # noqa: E501

        :return: The label of this Options9.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this Options9.

        Only valid for local builds   # noqa: E501

        :param label: The label of this Options9.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def platform(self):
        """Gets the platform of this Options9.  # noqa: E501

        Only valid for local builds   # noqa: E501

        :return: The platform of this Options9.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Options9.

        Only valid for local builds   # noqa: E501

        :param platform: The platform of this Options9.  # noqa: E501
        :type: str
        """
        allowed_values = ["ios", "android", "webplayer", "webgl", "standaloneosxintel", "standaloneosxintel64", "standaloneosxuniversal", "standalonewindows", "standalonewindows64", "standalonelinux", "standalonelinux64", "standalonelinuxuniversal"]  # noqa: E501
        if (self._configuration.client_side_validation and
                platform not in allowed_values):
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"  # noqa: E501
                .format(platform, allowed_values)
            )

        self._platform = platform

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
        if issubclass(Options9, dict):
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
        if not isinstance(other, Options9):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Options9):
            return True

        return self.to_dict() != other.to_dict()
