def Cal_prob_dominantAllele (homozygous_dominant, heterozygous, homozygous_recessive ):
    total = homozygous_dominant + heterozygous + homozygous_recessive
    
    child_homo_recess_prob = (homozygous_recessive / total) * ((homozygous_recessive - 1) / (total - 1))
    child_heter_prob = (heterozygous/total) * ((heterozygous-1)/(total-1))
    child_heter_homoRec_prob = (heterozygous/total) * (homozygous_recessive / (total-1)) + (homozygous_recessive/total)*(heterozygous/(total-1))
    
    all_homoRec_prob = child_homo_recess_prob + child_heter_prob*.25 + child_heter_homoRec_prob*.5
    
    atLeast_DomAll_prob = 1 - all_homoRec_prob
    return atLeast_DomAll_prob
    
reslt = Cal_prob_dominantAllele(30,21,16)
print(reslt)
