from category_encoders.backward_difference import BackwardDifferenceEncoder
from category_encoders.basen import BaseNEncoder
from category_encoders.binary import BinaryEncoder
from category_encoders.cat_boost import CatBoostEncoder
from category_encoders.hashing import HashingEncoder
from category_encoders.helmert import HelmertEncoder
from category_encoders.james_stein import JamesSteinEncoder
from category_encoders.leave_one_out import LeaveOneOutEncoder
from category_encoders.m_estimate import MEstimateEncoder
from category_encoders.one_hot import OneHotEncoder
from category_encoders.ordinal import OrdinalEncoder
from category_encoders.polynomial import PolynomialEncoder
from category_encoders.sum_coding import SumEncoder
from category_encoders.target_encoder import TargetEncoder
from category_encoders.woe import WOEEncoder


class CategoryEncoders:
    def __init__(self):
        pass

    # supervised encoders
    def target_encoder(self, X, y, cols=None):
        encoder = TargetEncoder(cols=cols)
        return encoder.fit_transform(X, y)

    def catboost_encoder(self, X, y, cols=None):
        encoder = CatBoostEncoder(cols=cols)
        return encoder.fit_transform(X, y)

    def james_stein_encoder(self, X, y, cols=None):
        encoder = JamesSteinEncoder(cols=cols)
        return encoder.fit_transform(X, y)

    def leaveone_encoder(self, X, y, cols=None):
        encoder = LeaveOneOutEncoder(cols=cols)
        return encoder.fit_transform(X, y)

    def mestimate_encoder(self, X, y, cols=None):
        encoder = MEstimateEncoder(cols=cols)
        return encoder.fit_transform(X, y)

    def weight_of_evidence_encoder(self, X, y, cols=None):
        encoder = WOEEncoder(cols=cols)
        return encoder.fit_transform(X, y)

    # unspervised encoders
    def binary_encoder(self, df, col=None):
        '''
        :param col: a list of columns to encode, if None, all string columns will be encoded.
        :param df:
        :return:
        '''
        encoder = BinaryEncoder(cols=col).fit(df)
        return encoder.transform(df)

    def backward_difference_encoder(self, df, col=None):
        '''

        :param df:
        :param col: a list of columns to encode, if None, all string columns will be encoded.
        :return:
        '''
        encoder = BackwardDifferenceEncoder(cols=col).fit(df)
        return encoder.transform(df)

    def basen_encoder(self, df, col=None):
        '''
        :param df:
        :param col: a list of columns to encode, if None, all string columns will be encoded.
        :return:
        '''
        encoder = BaseNEncoder(cols=col).fit(df)
        return encoder.transform(df)

    def hash_encoder(self, df, col=None):
        encoder = HashingEncoder(cols=col).fit(df)
        return encoder.transform(df)

    def helmert_encoder(self, df, col=None):
        encoder = HelmertEncoder(cols=col).fit(df)
        return encoder.transform(df)

    def one_hot_encoder(self, df, col=None):
        encoder = OneHotEncoder(cols=col).fit(df)
        return encoder.transform(df)

    def ordinal_encoder(self, df, col=None):
        encoder = OrdinalEncoder(cols=col).fit(df)
        return encoder.transform(df)

    def polynomial_encoder(self, df, col=None):
        encoder = PolynomialEncoder(cols=col).fit(df)
        return encoder.transform(df)

    def sum_encoder(self, df, col=None):
        encoder = SumEncoder(cols=col).fit(df)
        return encoder.transform(df)





