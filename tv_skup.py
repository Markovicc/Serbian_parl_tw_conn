# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 11:30:58 2017

@author: user
"""
import time
import tweepy
from tweepy import OAuthHandler
CONSUMER_KEY = 'eFnpkxeqNtSJ9h4bSd1me63zv'
CONSUMER_SECRET = 'qLzsWfYujDZHNDT0Z3Eqsf6BGcAobsCShFSQmSmadndlINLb78'
OAUTH_TOKEN = '836911248151281665-kYoueWxwQxL4aRKpiXj2FGijjn6i1Xk'
OAUTH_TOKEN_SECRET = 'rWbALCNrKmv3T2rrwyJiPF0MhOVLP3kXaoEVGYKdULeBi'
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)


final = ['Ceda_Jovanovic',
 'zorandirektno',
 'gjesic',
 'zigmanov',
 'jecazaric',
 'vukomand',
 'Sonja_Vlahovic',
 'MajaVidenovic',
 'torbicamb',
 'BgdSaska',
 'MarinikaTepic',
 'NemanjaSarovic',
 'dragansormaz',
 'Duca_Stojkovic',
 'stevanovicana7',
 'predsednikSRS',
 'Stevanovich_A',
  'MarijanNSS',
 'RakicKatarina',
 'VjericaR',
 'd_pavlovic',
 'pantovicognjen',
 'Vladimir_Orlic',
 'BoskoObradovic',
 'Jazilla',
 'DejanNikolic',
 'DusanORLDusan',
 'MilijaMiletic',
 'banem8',
 'mihailna',
 'aleksmark81',
 'vmarinkovic99',
 'marjanovic_v',
 'Lapcevicnis',
 'ZoranKrasic',
 'milankakaric',
 'ZeleniPoslanik',
 'dragomirkaric',
 'EnisImamovic',
 'marijanedic7',
 'DubravkaFilipov',
 'Kafa_sa_Djukom',
 'ZoranIga',
 'ZvonimirDjokic',
 'gordanacom',
 'radikalmiljan',
 'XXLTulip',
 'Corba44',
 'bukimont',
 'balshone',
 'misaizdaleka',
 'bauerivan',
 'nbozic',
 'Dragana_Barisic',
 'mbacevac',
 'aleksandrasrs',
 'MajaGojkovic',
 'AleksJerkov',
 'djordjenspm',
 'TatjanaMacura',
 'SasaRadulovich',
 'pasztorbalint',
 'micinzarko',
 'SrBaFilipovic',
 'Vladimir_Djuric',
 'Natasa_Vucko',
 'sanda_SRI',
 'linta_miodrag']


parovi = [(i,k) for i in final for k in final if i!=k]

for i in parovi:
    rez = api.show_friendship(source_screen_name=i[0], target_screen_name=i[1])
    following = rez[0].following
    follows = rez[0].followed_by
    print("%s following %s: %s" % (i[0], i[1], following))
    print("%s following %s: %s" % (i[1], i[0], follows))
    time.sleep(5)
    
    
def relacija_test(l):
    prati = []
    pracen = []
    for i in l:
        rez = api.show_friendship(source_screen_name=i[0], target_screen_name=i[1])
        prati.append(rez[0].following)
        pracen.append(rez[0].followed_by)
        time.sleep(5)
    return prati, pracen


def relacija(l):
    
    prati = []
    pracen = []
    par =[]
    for i in l:
        try:
            rez = api.show_friendship(source_screen_name=i[0], target_screen_name=i[1])
            prati.append(rez[0].following)
            pracen.append(rez[0].followed_by)
            par.append(i)
            time.sleep(5)

        except tweepy.TweepError as e:
            print(e.reason)
        
        except StopIteration:
            break
        
    return prati, pracen, par