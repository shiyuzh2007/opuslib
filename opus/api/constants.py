#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Matches to `opus_defines.h`"""

__author__ = 'Никита Кузнецов <self@svartalf.info>'
__copyright__ = 'Copyright (c) 2012, SvartalF'
__license__ = 'BSD 3-Clause License'


# No Error
OK = 0

# One or more invalid/out of range arguments
BAD_ARG = -1

# The mode struct passed is invalid
BUFFER_TOO_SMALL = -2

# The compressed data passed is corrupted
INVALID_PACKET = -4

# Invalid/unsupported request number
UNIMPLEMENTED = -5


# Pre-defined values for CTL interface

APPLICATION_VOIP = 2048
APPLICATION_AUDIO = 2049
APPLICATION_RESTRICTED_LOWDELAY = 2051

SIGNAL_MUSIC = 3002

# Values for the various encoder CTLs

SET_APPLICATION_REQUEST = 4000
GET_APPLICATION_REQUEST = 4001
SET_BITRATE_REQUEST = 4002
GET_BITRATE_REQUEST = 4003
SET_MAX_BANDWIDTH_REQUEST = 4004
GET_MAX_BANDWIDTH_REQUEST = 4005
SET_VBR_REQUEST = 4006
GET_VBR_REQUEST = 4007
SET_BANDWIDTH_REQUEST = 4008
GET_BANDWIDTH_REQUEST = 4009
SET_COMPLEXITY_REQUEST = 4010
GET_COMPLEXITY_REQUEST = 4011
SET_INBAND_FEC_REQUEST = 4012
GET_INBAND_FEC_REQUEST = 4013
SET_PACKET_LOSS_PERC_REQUEST = 4014
GET_PACKET_LOSS_PERC_REQUEST = 4015
SET_DTX_REQUEST = 4016
GET_DTX_REQUEST = 4017
SET_VBR_CONSTRAINT_REQUEST = 4020
GET_VBR_CONSTRAINT_REQUEST = 4021
SET_FORCE_CHANNELS_REQUEST = 4022
GET_FORCE_CHANNELS_REQUEST = 4023
SET_SIGNAL_REQUEST = 4024
GET_SIGNAL_REQUEST = 4025
GET_LOOKAHEAD_REQUEST = 4027
RESET_STATE = 4028
GET_SAMPLE_RATE_REQUEST = 4029
GET_FINAL_RANGE_REQUEST = 4031
GET_PITCH_REQUEST = 4033
SET_GAIN_REQUEST = 4034
GET_GAIN_REQUEST = 4045
SET_LSB_DEPTH_REQUEST = 4036
GET_LSB_DEPTH_REQUEST = 4037

AUTO = -1000

BANDWIDTH_NARROWBAND = 1101
BANDWIDTH_MEDIUMBAND = 1102
BANDWIDTH_WIDEBAND = 1103
BANDWIDTH_SUPERWIDEBAND = 1104
BANDWIDTH_FULLBAND = 1105
