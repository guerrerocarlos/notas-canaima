from django.db import models



class Autor(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name


class Nota(models.Model):

    def hace_cuanto(fecha):
        """
        Returns a humanized string representing time difference
        between now() and the input timestamp.
        
        The output rounds up to days, hours, minutes, or seconds.
        4 days 5 hours returns '4 days'
        0 days 4 hours 3 minutes returns '4 hours', etc...
	"""
    	import datetime	
	timestamp=fecha
	
    	timeDiff = datetime.datetime.now() - timestamp
    	days = timeDiff.days
    	hours = timeDiff.seconds/3600
   	minutes = timeDiff.seconds%3600/60
    	seconds = timeDiff.seconds%3600%60
    
	str = ""
    	tStr = ""
	return "Prueba"
    	if days > 0:
        	if days == 1:   tStr = "day"
        	else:           tStr = "days"
        	str = str + "%s %s" %(days, tStr)
        	return str
    	elif hours > 0:
        	if hours == 1:  tStr = "hour"
        	else:           tStr = "hours"
        	str = str + "%s %s" %(hours, tStr)
        	return str
    	elif minutes > 0:
        	if minutes == 1:tStr = "min"
        	else:           tStr = "mins"           
        	str = str + "%s %s" %(minutes, tStr)
        	return str
    	elif seconds > 0:
        	if seconds == 1:tStr = "sec"
        	else:           tStr = "secs"
        	str = str + "%s %s" %(seconds, tStr)
        	return str
    	else:
        	return None


    def __unicode__(self):
        return u'%s %s' % (self.titulo, self.autor)

    titulo = models.CharField(max_length=30)
    nota = models.CharField(max_length=500)
    autor=models.ForeignKey(Autor)
    fecha=models.DateTimeField(auto_now_add=True)


