#!/usr/bin/pythons.
# -*- coding: utf-8 -*-

# Importe
if 1 == 1:                        
    import tkinter as tk
    #from hdpitkinter import HdpiTk
    import time
    import requests
    from threading import Thread
    import hashlib
    import hmac

# Variablen
if 1==1:

    a_key = "---" 
    s_key = "---"

    base_url = "https://api.binance.com"
    
    # Variablen Farben
    rot = "#ffafa6"
    gruen = "#d9ffd9"
    blau = "#A9D0F5"

    # FOK toleranz
    fok_buy_tz = 1.001
    fok_sell_tz = 0.999

    # Sonstiges
    template_nr = 0

    # Expired pause
    pause_ex = 5


    def test():
        pass


# BOT FADEN
if 1==1:
    class bot_starten_thread(Thread):
        def run(self):
            global bot_start, bot_pause, new_bp, order_ok, r, mm_active

            # Variablen
            zeit_anfang = time.time()
            bot_start = 1
            order_ok = 0

            # Start Buttons
            b_bot_start.config (state="disabled")
            b_bot_start.config (bg="#b7d9b1")
            b_bot_stop.config (bg="#b7d9b1")
            
            # Zeitkorrektur
            timek()

            # FEAT Funds Control calculieren
            if b_feat_fcon_onoff1.cget("bg") == gruen:
                feat_fcon_cal1()


            # START FADEN
            while bot_start == 1:

                # Pause an
                bot_pause = 1
                if bot_start == 0:
                    break

                # 1 Zeitdifferenz ausrechnen Faden
                if 1==1:
                    pause_wert = float(e_sec_intervall.get())
                    
                    zeit_ende = time.time() - zeit_anfang - pause_wert
                    zeit_anfang = time.time()
                    l_bot_zeitd.configure (text="%.4f" % zeit_ende)

                # 2 Kurs holen
                if 1==1:
                    if b_fill_onoff.cget("bg")  == gruen:
                        api_price = "https://api.binance.com/api/v1/ticker/price?symbol=" + e_pair.get().upper()
                        try:
                            r = requests.get(url=api_price, timeout=4)
                            l_price.configure (text=float(r.json() ["price"]))
                        except:
                            try:
                                if r.text.find ("price") > 0:
                                    l_price.configure (bg="red")
                                    time.sleep (0.5)
                                    l_price.configure (bg="#B0E2FF")

                                else:

                                    t_log_all.insert ("1.0", r.text + "\n\n")
                                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  KURS HOLEN FAIL")
                            except:
                                t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  KURS HOLEN FAIL\n")

                # 2.5 FEAT MA FOLLOW
                if 1==1:
                    if b_feat_maf_onoff.cget("bg") == gruen:

                        if l_feat_maf_round_use.cget("text") == 0:
                            feat_maf_main()
                            l_feat_maf_round_use.configure (text=int(e_feat_maf_round.get()))
                        else:
                            l_feat_maf_round_use.configure (text=l_feat_maf_round_use.cget("text") - 1)
                    
                # 3 Prüfen BUY ACTIVE
                if (float(l_price.cget("text")) < float(e_main_price_buy.get())
                    and b_main_buy_onoff.cget("bg") == gruen
                    and b_funds_a2_onoff.cget("bg") == gruen):

                    # Prüfen Kapital vorhanden
                    kapi_vorhanden_buy()

                    if b_funds_a2_onoff.cget("bg") == gruen:

                        # Freigabe FEATS reseten
                        feat_fcon_buy = 0
                        feat_pcon_buy = 0

                        # FEAT Funds Control
                        if b_feat_fcon_onoff1.cget("bg") == rot:
                            feat_fcon_buy = 1
                        elif b_feat_fcon_onoff1.cget("bg") == gruen and b_feat_fcon_buy1.cget("bg") == gruen:
                            feat_fcon_buy = 1

                        # FEAT Price Control
                        if b_feat_pcon_onoff.cget("bg") == rot:
                            feat_pcon_buy = 1
                        else:
                            feat_pcon_main()

                        if b_feat_pcon_cal_buy.cget("bg") == gruen:
                            feat_pcon_buy = 1

                        # Freigabe FEATS prüfen
                        if feat_fcon_buy == 1 and feat_pcon_buy == 1:
                            # Multi Mix lvl prüfen
                            if b_main_price_buy_onoff.cget("bg") == gruen:
                                mm_active = 1
                                buy_active()
                            elif b_main_price_buy2_onoff.cget("bg") == gruen:
                                if float(l_price.cget("text")) < float(e_main_price_buy2.get()):
                                    mm_active = 2
                                    buy_active()
                            elif b_main_price_buy3_onoff.cget("bg") == gruen:
                                if float(l_price.cget("text")) < float(e_main_price_buy3.get()):
                                    mm_active = 3
                                    buy_active()
                            elif b_main_price_buy4_onoff.cget("bg") == gruen:
                                if float(l_price.cget("text")) < float(e_main_price_buy4.get()):
                                    mm_active = 4
                                    buy_active()
                            elif b_main_price_buy5_onoff.cget("bg") == gruen:
                                if float(l_price.cget("text")) < float(e_main_price_buy5.get()):
                                    mm_active = 5
                                    buy_active()

                # 4 Prüfen SELL ACTIVE
                if (float(l_price.cget("text")) > float(e_main_price_sell.get())
                    and b_main_sell_onoff.cget("bg") == gruen
                    and b_funds_a1_onoff.cget("bg") == gruen):

                    # Prüfen Kapital vorhanden
                    kapi_vorhanden_sell()

                    if b_funds_a1_onoff.cget("bg") == gruen:

                        # Freigabe FEATS reseten
                        feat_fcon_sell = 0
                        feat_pcon_sell = 0

                        # FEAT Funds Control
                        if b_feat_fcon_onoff1.cget("bg") == rot:
                            feat_fcon_sell = 1
                        elif b_feat_fcon_onoff1.cget("bg") == gruen and b_feat_fcon_sell1.cget("bg") == gruen:
                            feat_fcon_sell = 1

                        # FEAT Price Control
                        if b_feat_pcon_onoff.cget("bg") == rot:
                            feat_pcon_sell = 1
                        else:
                            feat_pcon_main()

                        if b_feat_pcon_cal_sell.cget("bg") == gruen:
                            feat_pcon_sell = 1

                        # Freigabe FEATS prüfen
                        if feat_fcon_sell == 1 and feat_pcon_sell == 1:
                            # Multi Mix lvl prüfen
                            if b_main_price_sell_onoff.cget("bg") == gruen:
                                mm_active = 1
                                sell_active()
                            elif b_main_price_sell2_onoff.cget("bg") == gruen:
                                if float(l_price.cget("text")) > float(e_main_price_sell2.get()):
                                    mm_active = 2
                                    sell_active()
                            elif b_main_price_sell3_onoff.cget("bg") == gruen:
                                if float(l_price.cget("text")) > float(e_main_price_sell3.get()):
                                    mm_active = 3
                                    sell_active()
                            elif b_main_price_sell4_onoff.cget("bg") == gruen:
                                if float(l_price.cget("text")) > float(e_main_price_sell4.get()):
                                    mm_active = 4
                                    sell_active()
                            elif b_main_price_sell5_onoff.cget("bg") == gruen:
                                if float(l_price.cget("text")) > float(e_main_price_sell5.get()):
                                    mm_active = 5
                                    sell_active()

                # 5 PAUSE
                if bot_pause == 1:   
                    
                    pausenzeit_anfang = time.time()
                    for i in range (0,20):
                        if bot_start == 0:
                            break
                        if time.time() > pausenzeit_anfang + float(e_sec_intervall.get()):
                            break
                        time.sleep (pause_wert / 20)

                # 5 Neue Werte nach Trade
                elif bot_pause == 0:
                    
                    # Order zurücksetzen
                    order_ok = 0

                    # neuer BP
                    e_main_bp.delete (0, "end")
                    e_main_bp.insert (0, new_bp)
                    main_bp_cal()
                    
                    # FEAT Funds Control Calculieren
                    if b_feat_fcon_onoff1.cget("bg") == gruen:
                        feat_fcon_cal1()

                    # FEAT MA FOLLOW ROUND setzen
                    l_feat_maf_round_use.configure (text=5)

                    # Autosave Datei erstellen
                    autosave_thread().start()
                    
            # Bot Stopen
            b_bot_start.config (state="normal")
            b_bot_start.config (bg="#cb8d73")
            b_bot_stop.config (bg="#cb8d73")

def buy_active():
    global bot_pause, new_bp, send_side, amount, send_price, order_ok, mm_active

    # SIM
    if b_bot_sim_onoff.cget("bg") == gruen:

        # Multi Mix Level 1
        if mm_active == 1:
            # BUY ORDER LEVEL 1
            buy_betrag = e_main_amount_buy.get()
            buy_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_buy.get()) / float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            buy_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()



            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_buy.get())
            
            # counter
            wert = int(e_counter_buy.get())
            e_counter_buy.delete (0, "end")
            e_counter_buy.insert (0, wert + 1)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 1)


        # Multi Mix Level 2
        elif mm_active == 2:
            # BUY ORDER LEVEL 1
            buy_betrag = e_main_amount_buy.get()
            buy_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_buy.get()) / float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            buy_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            
            # BUY ORDER LEVEL 2
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy2.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()



            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_buy2.get())
            
            # counter
            wert = int(e_counter_buy.get())
            e_counter_buy.delete (0, "end")
            e_counter_buy.insert (0, wert + 2)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 2)


        # Multi Mix Level 3
        elif mm_active == 3:
            # BUY ORDER LEVEL 1
            buy_betrag = e_main_amount_buy.get()
            buy_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_buy.get()) / float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            buy_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            
            # BUY ORDER LEVEL 2
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy2.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()
            
            # BUY ORDER LEVEL 3
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy3.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()



            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_buy3.get())
            
            # counter
            wert = int(e_counter_buy.get())
            e_counter_buy.delete (0, "end")
            e_counter_buy.insert (0, wert + 3)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 3)

        # Multi Mix Level 4
        elif mm_active == 4:
            # BUY ORDER LEVEL 1
            buy_betrag = e_main_amount_buy.get()
            buy_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_buy.get()) / float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            buy_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            
            # BUY ORDER LEVEL 2
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy2.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()
            
            # BUY ORDER LEVEL 3
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy3.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # BUY ORDER LEVEL 4
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy4.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy4.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy4.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()



            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_buy4.get())
            
            # counter
            wert = int(e_counter_buy.get())
            e_counter_buy.delete (0, "end")
            e_counter_buy.insert (0, wert + 4)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 4)


        # Multi Mix Level 5
        elif mm_active == 5:
            # BUY ORDER LEVEL 1
            buy_betrag = e_main_amount_buy.get()
            buy_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_buy.get()) / float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            buy_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            
            # BUY ORDER LEVEL 2
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy2.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()
            
            # BUY ORDER LEVEL 3
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy3.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # BUY ORDER LEVEL 4
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy4.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy4.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy4.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # BUY ORDER LEVEL 5
            buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy5.get()) / 100)) - 100) * (-1))

            # Amount zum A1 hinzufügen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
            
            # vom A2 abziehen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))

            # STATS
            funds_cal()
            buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy5.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " BUY  " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                        + str(e_main_price_buy5.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()



            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_buy5.get())
            
            # counter
            wert = int(e_counter_buy.get())
            e_counter_buy.delete (0, "end")
            e_counter_buy.insert (0, wert + 5)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 5)

    # REAL
    elif b_bot_sim_onoff.cget("bg") == rot:

        # Multi Mix Level 1
        if mm_active == 1:

            # Variablen
            send_side = "BUY"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_buy_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_buy.get()) / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # BUY ORDER
                buy_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                buy_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                buy_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))

                # Amount zum A1 hinzufügen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
                
                # vom A2 abziehen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))


                # STATS
                funds_cal()
                buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()



                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_buy.get())

                # counter
                wert = int(e_counter_buy.get())
                e_counter_buy.delete (0, "end")
                e_counter_buy.insert (0, wert + 1)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 1)

        # Multi Mix Level 2
        elif mm_active == 2:
            
            # Variablen
            send_side = "BUY"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_buy_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_buy.get()) * 2 / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # FUNDS UPDATE
                buy_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                buy_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                buy_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))

                # Amount zum A1 hinzufügen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
                
                # vom A2 abziehen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))
                funds_cal()

                # BUY ORDER 1
                buy_betrag = b_main_am_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / 2)
                buy_amount = b_funds_a1_k.cget("text") % (float(r.json() ["executedQty"]) / 2)
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))



                # STATS
                buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # BUY ORDER 2
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy2.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()




                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_buy2.get())

                # counter
                wert = int(e_counter_buy.get())
                e_counter_buy.delete (0, "end")
                e_counter_buy.insert (0, wert + 2)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 2)

        # Multi Mix Level 3
        elif mm_active == 3:
            
            # Variablen
            send_side = "BUY"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_buy_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_buy.get()) * 3 / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # FUNDS UPDATE
                buy_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                buy_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                buy_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))

                # Amount zum A1 hinzufügen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
                
                # vom A2 abziehen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))
                funds_cal()

                # BUY ORDER 1
                buy_betrag = b_main_am_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / 3)
                buy_amount = b_funds_a1_k.cget("text") % (float(r.json() ["executedQty"]) / 3)
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))



                # STATS
                buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # BUY ORDER 2
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy2.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # BUY ORDER 3
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy3.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_buy3.get())

                # counter
                wert = int(e_counter_buy.get())
                e_counter_buy.delete (0, "end")
                e_counter_buy.insert (0, wert + 3)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 3)

        # Multi Mix Level 4
        elif mm_active == 4:
            
            # Variablen
            send_side = "BUY"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_buy_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_buy.get()) * 4 / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # FUNDS UPDATE
                buy_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                buy_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                buy_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))

                # Amount zum A1 hinzufügen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
                
                # vom A2 abziehen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))
                funds_cal()

                # BUY ORDER 1
                buy_betrag = b_main_am_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / 4)
                buy_amount = b_funds_a1_k.cget("text") % (float(r.json() ["executedQty"]) / 4)
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))



                # STATS
                buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # BUY ORDER 2
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy2.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # BUY ORDER 3
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy3.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # BUY ORDER 4
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy4.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy4.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy4.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_buy4.get())

                # counter
                wert = int(e_counter_buy.get())
                e_counter_buy.delete (0, "end")
                e_counter_buy.insert (0, wert + 4)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 4)

        # Multi Mix Level 5
        elif mm_active == 5:
            
            # Variablen
            send_side = "BUY"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_buy_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_buy.get()) * 5 / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # FUNDS UPDATE
                buy_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                buy_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                buy_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))

                # Amount zum A1 hinzufügen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert + float(buy_amount)))
                
                # vom A2 abziehen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert - float(buy_betrag)))
                funds_cal()

                # BUY ORDER 1
                buy_betrag = b_main_am_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / 5)
                buy_amount = b_funds_a1_k.cget("text") % (float(r.json() ["executedQty"]) / 5)
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy.get()) / 100)) - 100) * (-1))



                # STATS
                buy_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(buy_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # BUY ORDER 2
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy2.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy2.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # BUY ORDER 3
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy3.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy3.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # BUY ORDER 4
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy4.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy4.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy4.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # BUY ORDER 5
                buy_diff_pro = "%.3f" % (((float(buy_price) / (float(e_main_price_buy5.get()) / 100)) - 100) * (-1))

                # STATS
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy5.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " BUY   " + str(buy_betrag) + "\t" +  str(buy_amount) + "\t" +  str(buy_price) + "\t" + "  "
                                            + str(e_main_price_buy5.get())  + "\t" +  str(buy_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   buy_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()




                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_buy5.get())

                # counter
                wert = int(e_counter_buy.get())
                e_counter_buy.delete (0, "end")
                e_counter_buy.insert (0, wert + 5)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 5)

def sell_active():
    global bot_pause, new_bp, send_side, amount, send_price, order_ok, mm_active

    # SIM
    if b_bot_sim_onoff.cget("bg") == gruen:

        # Multi Mix Level 1
        if mm_active == 1:
            # SELL ORDER LEVEL 1
            sell_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_sell.get()) / float(l_price.cget("text"))))
            sell_betrag = b_funds_a2_k.cget("text") % ((float(sell_amount) * float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            sell_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()



            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_sell.get())   
            # counter
            wert = int(e_counter_sell.get())
            e_counter_sell.delete (0, "end")
            e_counter_sell.insert (0, wert + 1)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 1)

        # Multi Mix Level 2
        elif mm_active == 2:
            # SELL ORDER LEVEL 1
            sell_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_sell.get()) / float(l_price.cget("text"))))
            sell_betrag = b_funds_a2_k.cget("text") % ((float(sell_amount) * float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            sell_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # SELL ORDER LEVEL 2
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell2.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()


            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_sell2.get())

            # counter
            wert = int(e_counter_sell.get())
            e_counter_sell.delete (0, "end")
            e_counter_sell.insert (0, wert + 2)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 2)


        # Multi Mix Level 3
        elif mm_active == 3:
            # SELL ORDER LEVEL 1
            sell_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_sell.get()) / float(l_price.cget("text"))))
            sell_betrag = b_funds_a2_k.cget("text") % ((float(sell_amount) * float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            sell_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # SELL ORDER LEVEL 2
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell2.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()


            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_sell2.get())

            # SELL ORDER LEVEL 3
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell3.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()


            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_sell3.get())

            # counter
            wert = int(e_counter_sell.get())
            e_counter_sell.delete (0, "end")
            e_counter_sell.insert (0, wert + 3)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 3)

        # Multi Mix Level 4
        elif mm_active == 4:
            # SELL ORDER LEVEL 1
            sell_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_sell.get()) / float(l_price.cget("text"))))
            sell_betrag = b_funds_a2_k.cget("text") % ((float(sell_amount) * float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            sell_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # SELL ORDER LEVEL 2
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell2.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()


            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_sell2.get())

            # SELL ORDER LEVEL 3
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell3.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # SELL ORDER LEVEL 4
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell4.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell4.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell4.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()



            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_sell4.get())

            # counter
            wert = int(e_counter_sell.get())
            e_counter_sell.delete (0, "end")
            e_counter_sell.insert (0, wert + 4)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 4)

        # Multi Mix Level 5
        elif mm_active == 5:
            # SELL ORDER LEVEL 1
            sell_amount = b_funds_a1_k.cget("text") % ((float(e_main_amount_sell.get()) / float(l_price.cget("text"))))
            sell_betrag = b_funds_a2_k.cget("text") % ((float(sell_amount) * float(l_price.cget("text"))) * (1 - float(e_main_fees.get()) / 100))
            sell_price = b_main_bp_k.cget("text") % float(l_price.cget("text"))
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # SELL ORDER LEVEL 2
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell2.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_sell2.get())

            # SELL ORDER LEVEL 3
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell3.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # SELL ORDER LEVEL 4
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell4.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell4.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell4.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # SELL ORDER LEVEL 5
            sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell5.get()) / 100)) - 100) 

            # von A1 abziehen
            wert = float(e_funds_a1.get())
            e_funds_a1.delete (0, "end")
            e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
            
            # zu A2 hinzufügen
            wert = float(e_funds_a2.get())
            e_funds_a2.delete (0, "end")
            e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))

            # STATS
            funds_cal()
            sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
            t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell5.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

            datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
            datei.write (time.strftime("%d %H:%M") + " SELL " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  " 
                                        + str(e_main_price_sell5.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                        + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                        + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
            datei.close()

            # erfolgreicher Trade
            bot_pause = 0
            new_bp = float(e_main_price_sell5.get())

            # counter
            wert = int(e_counter_sell.get())
            e_counter_sell.delete (0, "end")
            e_counter_sell.insert (0, wert + 5)
            wert = int(e_counter_gesamt.get())
            e_counter_gesamt.delete (0, "end")
            e_counter_gesamt.insert (0, wert + 5)

    # REAL
    elif b_bot_sim_onoff.cget("bg") == rot:
        
        # Multi Mix Level 1
        if mm_active == 1:

            # Variablen
            send_side = "SELL"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_sell_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_sell.get()) / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # SELL ORDER
                sell_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                sell_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                sell_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 

                # von A1 abziehen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
                
                # zu A2 hinzufügen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))


                # STATS
                funds_cal()
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()



                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_sell.get())

                # counter
                wert = int(e_counter_sell.get())
                e_counter_sell.delete (0, "end")
                e_counter_sell.insert (0, wert + 1)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 1)

        # Multi Mix Level 2
        elif mm_active == 2:

            # Variablen
            send_side = "SELL"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_sell_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_sell.get()) * 2 / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # FUNDS UPDATE
                sell_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                sell_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                sell_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))

                # von A1 abziehen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
                
                # zu A2 hinzufügen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))
                funds_cal()


                # SELL ORDER 1
                sell_betrag = b_main_am_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / 2)
                sell_amount = b_funds_a1_k.cget("text") % (float(r.json() ["executedQty"]) / 2)
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # SELL ORDER 2
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell2.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()



                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_sell2.get())

                # counter
                wert = int(e_counter_sell.get())
                e_counter_sell.delete (0, "end")
                e_counter_sell.insert (0, wert + 2)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 2)

        # Multi Mix Level 3
        elif mm_active == 3:

            # Variablen
            send_side = "SELL"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_sell_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_sell.get()) * 3 / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # FUNDS UPDATE
                sell_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                sell_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                sell_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))

                # von A1 abziehen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
                
                # zu A2 hinzufügen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))
                funds_cal()


                # SELL ORDER 1
                sell_betrag = b_main_am_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / 3)
                sell_amount = b_funds_a1_k.cget("text") % (float(r.json() ["executedQty"]) / 3)
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # SELL ORDER 2
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell2.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # SELL ORDER 3
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell3.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()



                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_sell3.get())

                # counter
                wert = int(e_counter_sell.get())
                e_counter_sell.delete (0, "end")
                e_counter_sell.insert (0, wert + 3)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 3)

        # Multi Mix Level 4
        elif mm_active == 4:

            # Variablen
            send_side = "SELL"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_sell_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_sell.get()) * 4 / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # FUNDS UPDATE
                sell_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                sell_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                sell_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))

                # von A1 abziehen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
                
                # zu A2 hinzufügen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))
                funds_cal()


                # SELL ORDER 1
                sell_betrag = b_main_am_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / 4)
                sell_amount = b_funds_a1_k.cget("text") % (float(r.json() ["executedQty"]) / 4)
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # SELL ORDER 2
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell2.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # SELL ORDER 3
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell3.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # SELL ORDER 4
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell4.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell4.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell4.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()




                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_sell4.get())

                # counter
                wert = int(e_counter_sell.get())
                e_counter_sell.delete (0, "end")
                e_counter_sell.insert (0, wert + 4)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 4)

        # Multi Mix Level 5
        elif mm_active == 5:

            # Variablen
            send_side = "SELL"
            send_price = b_main_bp_k.cget("text") % (float(l_price.cget("text")) * fok_sell_tz)
            amount = b_funds_a1_k.cget("text") % (float(e_main_amount_sell.get()) * 5 / float(send_price))

            # Order senden
            send_order()

            # Wenn Order FILLED
            if order_ok == 1:

                # FUNDS UPDATE
                sell_betrag = b_main_am_k.cget("text") % float(r.json() ["cummulativeQuoteQty"])
                sell_amount = b_funds_a1_k.cget("text") % float(r.json() ["executedQty"])
                sell_price = b_main_bp_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / float(r.json() ["executedQty"]))

                # von A1 abziehen
                wert = float(e_funds_a1.get())
                e_funds_a1.delete (0, "end")
                e_funds_a1.insert (0, b_funds_a1_k.cget("text") % (wert - float(sell_amount)))
                
                # zu A2 hinzufügen
                wert = float(e_funds_a2.get())
                e_funds_a2.delete (0, "end")
                e_funds_a2.insert (0, b_funds_a2_k.cget("text") % (wert + float(sell_betrag)))
                funds_cal()


                # SELL ORDER 1
                sell_betrag = b_main_am_k.cget("text") % (float(r.json() ["cummulativeQuoteQty"]) / 4)
                sell_amount = b_funds_a1_k.cget("text") % (float(r.json() ["executedQty"]) / 4)
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # SELL ORDER 2
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell2.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell2.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # SELL ORDER 3
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell3.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell3.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # SELL ORDER 4
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell4.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell4.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell4.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()

                # SELL ORDER 5
                sell_diff_pro = "%.3f" % ((float(sell_price) / (float(e_main_price_sell5.get()) / 100)) - 100) 


                # STATS
                sell_amount_wert = b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(sell_price))
                t_log_stats1.insert ("1.0", (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell5.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n"))

                datei = open ("log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt" , "a")
                datei.write (time.strftime("%d %H:%M") + " SELL  " + str(sell_betrag) + "\t" +  str(sell_amount) + "\t" +  str(sell_price) + "\t" + "  "
                                            + str(e_main_price_sell5.get())  + "\t" +  str(sell_diff_pro)[:-1]  + "\t" + "  "
                                            + str(e_funds_a1.get()) + "(" +   sell_amount_wert + ")" + "\t" + str(e_funds_a2.get()) + "\t" + "  "
                                            + str(l_kapi_a1.cget("text"))  + "\t" +  str(l_kapi_a2.cget("text")) + "\n")
                datei.close()


                # erfolgreicher Trade
                bot_pause = 0
                new_bp = float(e_main_price_sell5.get())

                # counter
                wert = int(e_counter_sell.get())
                e_counter_sell.delete (0, "end")
                e_counter_sell.insert (0, wert + 5)
                wert = int(e_counter_gesamt.get())
                e_counter_gesamt.delete (0, "end")
                e_counter_gesamt.insert (0, wert + 5)

def send_order():
    global send_side, amount, send_price, order_ok, r

    wait = 10
    wait_pause = 1

    while wait > 0:
        if bot_start == 0:
            break

        t = (int("%.0f" % time.time()) * 1000) + int(b_timek.cget("text"))
        t_str = str(t)

        order = "/api/v3/order"

        first = "?"
        symbol = "symbol=" + e_pair.get().upper()
        side = "&side=" + send_side
        typee = "&type=LIMIT"
        timeinforce = "&timeInForce=FOK"
        qty = "&quantity=" + str(amount)
        price = "&price=" + send_price
        zeit = "&timestamp=" + t_str

        query = symbol + side + typee + timeinforce + qty + price + zeit

        signature = hmac.new(s_key.encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()

        sign_end = "&signature=" + signature

        url_rdy = base_url + order + first + query + sign_end

        header = {'X-MBX-APIKEY' : a_key}
        try:
            r = requests.post (url_rdy, headers=header, timeout=15)

            if r.json() ["status"] == "FILLED":

                if b_bot_docu_onoff.cget ("bg") == gruen:
                    t_log_all.insert ("1.0", r.text + "\n")              
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: FILLED\n")

                order_ok = 1
                wait = 0

            
            elif r.json() ["status"] == "EXPIRED":
                if b_bot_docu_onoff.cget ("bg") == gruen:
                    t_log_all.insert ("1.0", r.text + "\n")
                    t_log_all.insert ("1.0", "Amount:" + str(amount) + "   Preis:" + str(send_price) + "   Betrag:" +  b_funds_a2_k.cget("text") % (float(amount) * float(send_price)) + "\n")
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: EXPIRED" + "\n")

                # Preis/Amount anpassen
                if send_side == "BUY":
                    """
                    send_price_test = b_main_bp_k.cget("text") % (float(send_price) * fok_buy_tz)
                    if float(send_price_test) < float(e_main_price_buy.get()):
                        send_price = b_main_bp_k.cget("text") % (float(send_price) * fok_buy_tz)
                        amount = b_funds_a1_k.cget("text") % (float(e_main_amount_buy.get()) / (float(send_price) * fok_buy_tz))
                        wait_pause = 0
                        time.sleep (0.3)
                        wait -= 1
                        if wait == 0:
                            t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: EXPIRED 20SEC PAUSE" + "\n")
                            for i in range (0,20):
                                if bot_start == 0:
                                    break
                                time.sleep (1)
                    else:
                    """
                    wait = 0
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: EXPIRED  " + str(pause_ex) + " SEC PAUSE" + "\n")
                    for i in range (0, pause_ex):
                        if bot_start == 0:
                            break
                        time.sleep (1)


                elif send_side == "SELL":
                    """
                    send_price_test = b_main_bp_k.cget("text") % (float(send_price) * fok_sell_tz)
                    if float(send_price_test) > float(e_main_price_sell.get()):
                        send_price = b_main_bp_k.cget("text") % (float(send_price) * fok_sell_tz)
                        amount = b_funds_a1_k.cget("text") % (float(e_main_amount_sell.get()) / (float(send_price) * fok_sell_tz))
                        wait_pause = 0
                        time.sleep (0.3)
                        wait -= 1
                        if wait == 0:
                            t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: EXPIRED 20SEC PAUSE" + "\n")
                            for i in range (0,20):
                                if bot_start == 0:
                                    break
                                time.sleep (1)
                    else:
                    """
                    wait = 0
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: EXPIRED  " + str(pause_ex) + " SEC PAUSE" + "\n")
                    for i in range (0, pause_ex):
                        if bot_start == 0:
                            break
                        time.sleep (1)



            else:
                try:
                    wait = 0
                    t_log_all.insert ("1.0", r.text + "\n")              
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: FAIL\n")
                except:
                    wait = 0
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: KRIT FAIL\n")



        except:

            if bot_start == 0:
                break
            
            try:
                t_log_all.insert ("1.0", r.text + "\n")              
                t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  STATUS: FAIL\n")

                # Wenn keine Funds
                if r.text.find ("insufficient balance") > -1:
                    if send_side == "BUY":
                        b_funds_a2_onoff.configure (bg=rot)
                    elif send_side == "SELL":
                        b_funds_a1_onoff.configure (bg=rot)
                
                # Wenn Except Timestamp dann Zeitkorrektur
                elif r.text.find ("Timestamp") > 0:
                    timek()
                    wait_pause = 0

                # Geringer Amount
                elif r.text.find ("MIN_NOTIONAL") > 0:
                    t_log_all.insert ("1.0", "Amount:" + str(amount) + "   Preis:" + str(send_price) + "   Betrag:" +  b_funds_a2_k.cget("text") % (float(amount) * float(send_price)) + "\n")
                    amount = b_funds_a1_k.cget("text") % (float(amount) * 1.01)
                    wait_pause = 0     
                    time.sleep (1)

                # zu weit weg vom Market Preis
                elif r.text.find ("PRICE_FILTER") > 0:
                    for i in range (0,5):
                        if bot_start == 0:
                            break
                        time.sleep (1)
                    return

                if wait > 1:
                    if wait_pause == 1:
                        for i in range (0,5):
                            if bot_start == 0:
                                break
                            time.sleep (1)
                    wait -= 1
                
                else:
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  BOT ORDER FAIL PAUSE 3 min\n\n") 
                    
                    for i in range (0,180):
                        if bot_start == 0:
                            break
                        time.sleep (1)
                    wait = 10
            except:
                t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  BOT ORDER KRIT FAIL PAUSE 3min\n\n") 
                
                for i in range (0,180):
                    if bot_start == 0:
                        break
                    time.sleep (1)
                wait = 10

# tkinter Fenster---------------------------------------------------------------------------
f = tk.Tk()
#f = HdpiTk()
f.title ("Free Grid Bot")
f.geometry ("1600x900+200+60")

# STATS
if 1==1:
    #Hintergrund
    area_stats = tk.Label (f,relief="ridge", bg="#d0fff1")
    area_stats.place (x=15, y=10, width=665, height=30)

    def stats_clear():

        t_log_stats1.delete ("1.0", "end")

    def stats_load():

        t_log_stats1.delete ("1.0", "end")

        # Datei öffnen
        liste_s1 = []
        try:
            f = open ("./log/bot1/trades_" + b_nbot_template.cget ("text") + ".txt", "r")
            liste_s1 = list(f)
            f.close()
        except:
            return

        for i in range (0,len(liste_s1)):

            zeile = liste_s1[i]

            t_log_stats1.insert ("1.0", zeile)

    t_log_stats1 = tk.Text (f, font=('Courier New', 16, 'bold'), bg="#d0d0d0")
    t_log_stats1.place (x=15, y=600, width=1570, height=300)

# SAVE (rechte Seite grünes Feld)
if 1==1:

    # Hintergrund
    area1_bg = tk.Label (f,relief="ridge", bg="#D8F6CE")
    area1_bg.place (x=1430, y=10, width=155, height=590)

    # Credits
    if 1==1:
        coord_x = 1435
        coord_y = 20

        l_youtube = tk.Label(f, text="Youtube\ntutorials:\nMK Strategies", font=('TkDefaultFont', 14, 'bold'),relief="ridge")
        l_youtube.place (x=coord_x, y=coord_y, width=145, height=90)

        l_telegram = tk.Label(f, text="Telegram:  t.me/\nshababs_botten", font=('TkDefaultFont', 13, 'bold'),relief="ridge")
        l_telegram.place (x=coord_x, y=coord_y + 100, width=145, height=50)



    # SAVE
    if 1==1:

        coord_x = 15
        coord_y = 10

        # LOAD / SAVE
        if 1==1:
            coord_x = 1440
            coord_y = 530

            def para_out():

                t_tools_save.delete ("1.0", "end")

                # 1 PAIR
                t_tools_save.insert ("end", str(e_pair.get()) + "\n")
                # 2 Intervall sec
                t_tools_save.insert ("end", str(e_sec_intervall.get()) + "\n")
                # 3 Main Amount komma
                t_tools_save.insert ("end", str(b_main_am_k.cget("text")) + "\n")
                # 4 Main Buy Amount
                t_tools_save.insert ("end", str(e_main_amount_buy.get()) + "\n")
                # 5 Main Buy onoff
                t_tools_save.insert ("end", str(b_main_buy_onoff.cget("bg")) + "\n")
                # 6 Main Buy price
                t_tools_save.insert ("end", str(e_main_price_buy.get()) + "\n")
                # 7 Main Buy prozente
                t_tools_save.insert ("end", str(e_main_pro_buy.get()) + "\n")
                # 8 Main BP
                t_tools_save.insert ("end", str(e_main_bp.get()) + "\n")
                # 9 Main BP komma
                t_tools_save.insert ("end", str(b_main_bp_k.cget("text")) + "\n")
                # 10 Main Sell Amount
                t_tools_save.insert ("end", str(e_main_amount_sell.get()) + "\n")
                # 11 Main Sell onoff
                t_tools_save.insert ("end", str(b_main_sell_onoff.cget("bg")) + "\n")
                # 12 Main Sell price
                t_tools_save.insert ("end", str(e_main_price_sell.get()) + "\n")
                # 13 Main Sell prozente
                t_tools_save.insert ("end", str(e_main_pro_sell.get()) + "\n")
                # 14 Funds A2 Amount
                t_tools_save.insert ("end", str(e_funds_a2.get()) + "\n")
                # 15 Funds A2 komma
                t_tools_save.insert ("end", str(b_funds_a2_k.cget("text")) + "\n")
                # 16 Funds A1 Amount
                t_tools_save.insert ("end", str(e_funds_a1.get()) + "\n")
                # 17 Funds A1 komma
                t_tools_save.insert ("end", str(b_funds_a1_k.cget("text")) + "\n")
                # 18 Counter buy
                t_tools_save.insert ("end", str(e_counter_buy.get()) + "\n")
                # 19 Counter gesamt
                t_tools_save.insert ("end", str(e_counter_gesamt.get()) + "\n")
                # 20 Counter sell
                t_tools_save.insert ("end", str(e_counter_sell.get()) + "\n")
                # 21 Fees
                t_tools_save.insert ("end", str(e_main_fees.get()) + "\n")
                # 22 FEAT FUNDS CONTROL 1  ONOFF
                t_tools_save.insert ("end", str(b_feat_fcon_onoff1.cget("bg")) + "\n")
                # 23 FEAT FUNDS CONTROL 1  ASSET
                t_tools_save.insert ("end", str(b_feat_fcon_asset1.cget("text")) + "\n")
                # 24 FEAT FUNDS CONTROL 1  OVER/UNDER
                t_tools_save.insert ("end", str(b_feat_fcon_over1.cget("text")) + "\n")
                # 25 FEAT FUNDS CONTROL 1  BETRAG
                t_tools_save.insert ("end", str(e_feat_fcon_funds1.get()) + "\n")
                # 26 FEAT FUNDS CONTROL 1  START/STOP
                t_tools_save.insert ("end", str(b_feat_fcon_start1.cget("text")) + "\n")
                # 27 FEAT FUNDS CONTROL 1  TRADE
                t_tools_save.insert ("end", str(b_feat_fcon_trade1.cget("text")) + "\n")
                # 28 SIM ONOFF
                t_tools_save.insert ("end", str(b_bot_sim_onoff.cget("bg")) + "\n")
                # 29 DOCU ONOFF
                t_tools_save.insert ("end", str(b_bot_docu_onoff.cget("bg")) + "\n")
                # 30 FEAT PRICE CONTROL ONOFF
                t_tools_save.insert ("end", str(b_feat_pcon_onoff.cget("bg")) + "\n")
                # 31 FEAT PRICE CONTROL UNDER PRICE
                t_tools_save.insert ("end", str(e_feat_pcon_u_price.get()) + "\n")
                # 32 FEAT PRICE CONTROL UNDER BUY
                t_tools_save.insert ("end", str(b_feat_pcon_u_buy.cget("bg")) + "\n")
                # 33 FEAT PRICE CONTROL UNDER SELL
                t_tools_save.insert ("end", str(b_feat_pcon_u_sell.cget("bg")) + "\n")
                # 34 FEAT PRICE CONTROL UNDER ELSE ONOFF
                t_tools_save.insert ("end", str(b_feat_pcon_u_e_onoff.cget("bg")) + "\n")
                # 35 FEAT PRICE CONTROL UNDER ELSE BUY
                t_tools_save.insert ("end", str(b_feat_pcon_u_e_buy.cget("bg")) + "\n")
                # 36 FEAT PRICE CONTROL UNDER ELSE SELL
                t_tools_save.insert ("end", str(b_feat_pcon_u_e_sell.cget("bg")) + "\n")
                # 37 FEAT PRICE CONTROL OVER PRICE
                t_tools_save.insert ("end", str(e_feat_pcon_o_price.get()) + "\n")
                # 38 FEAT PRICE CONTROL OVER BUY
                t_tools_save.insert ("end", str(b_feat_pcon_o_buy.cget("bg")) + "\n")
                # 39 FEAT PRICE CONTROL OVER SELL
                t_tools_save.insert ("end", str(b_feat_pcon_o_sell.cget("bg")) + "\n")
                # 40 FEAT PRICE CONTROL OVER ELSE ONOFF
                t_tools_save.insert ("end", str(b_feat_pcon_o_e_onoff.cget("bg")) + "\n")
                # 41 FEAT PRICE CONTROL OVER ELSE BUY
                t_tools_save.insert ("end", str(b_feat_pcon_o_e_buy.cget("bg")) + "\n")
                # 42 FEAT PRICE CONTROL OVER ELSE SELL
                t_tools_save.insert ("end", str(b_feat_pcon_o_e_sell.cget("bg")) + "\n")
                # 43 Main Buy price 2
                t_tools_save.insert ("end", str(e_main_price_buy2.get()) + "\n")
                # 44 Main Buy price 3
                t_tools_save.insert ("end", str(e_main_price_buy3.get()) + "\n")
                # 45 Main Sell price 2
                t_tools_save.insert ("end", str(e_main_price_sell2.get()) + "\n")
                # 46 Main Sell price 3
                t_tools_save.insert ("end", str(e_main_price_sell3.get()) + "\n")
                # 47 Price Buy onoff 1
                t_tools_save.insert ("end", str(b_main_price_buy_onoff.cget("bg")) + "\n")
                # 48 Price Buy onoff 2
                t_tools_save.insert ("end", str(b_main_price_buy2_onoff.cget("bg")) + "\n")
                # 49 Price Buy onoff 3
                t_tools_save.insert ("end", str(b_main_price_buy3_onoff.cget("bg")) + "\n")
                # 50 Price Sell onoff 1
                t_tools_save.insert ("end", str(b_main_price_sell_onoff.cget("bg")) + "\n")
                # 51 Price Sell onoff 2
                t_tools_save.insert ("end", str(b_main_price_sell2_onoff.cget("bg")) + "\n")
                # 52 Price Sell onoff 3
                t_tools_save.insert ("end", str(b_main_price_sell3_onoff.cget("bg")) + "\n")
                # 53 Main Buy price 4
                t_tools_save.insert ("end", str(e_main_price_buy4.get()) + "\n")
                # 54 Main Buy price 5
                t_tools_save.insert ("end", str(e_main_price_buy5.get()) + "\n")
                # 55 Main sell price 4
                t_tools_save.insert ("end", str(e_main_price_sell4.get()) + "\n")
                # 56 Main sell price 5
                t_tools_save.insert ("end", str(e_main_price_sell5.get()) + "\n")
                # 57 Price Buy onoff 4
                t_tools_save.insert ("end", str(b_main_price_buy4_onoff.cget("bg")) + "\n")
                # 58 Price Buy onoff 5
                t_tools_save.insert ("end", str(b_main_price_buy5_onoff.cget("bg")) + "\n")
                # 59 Price sell onoff 4
                t_tools_save.insert ("end", str(b_main_price_sell4_onoff.cget("bg")) + "\n")
                # 60 Price sell onoff 5
                t_tools_save.insert ("end", str(b_main_price_sell5_onoff.cget("bg")) + "\n")
                # 61 FEAT MA FOLLOW ONOFF
                t_tools_save.insert ("end", str(b_feat_maf_onoff.cget("bg")) + "\n")
                # 62 FEAT MA FOLLOW INTERVALL
                t_tools_save.insert ("end", str(b_feat_maf_interval.cget("text")) + "\n")
                # 63 FEAT MA FOLLOW LIMIT
                t_tools_save.insert ("end", str(e_feat_maf_limit.get()) + "\n")
                # 64 FEAT MA FOLLOW KOMMA
                t_tools_save.insert ("end", str(b_feat_maf_k.cget("text")) + "\n")
                # 65 FEAT MA FOLLOW ROUND
                t_tools_save.insert ("end", str(e_feat_maf_round.get()) + "\n")
                # 66 FEAT MA FOLLOW LINE1 PRO
                t_tools_save.insert ("end", str(e_feat_maf_line1_pro.get()) + "\n")
                # 67 FEAT MA FOLLOW LINE1 BUY
                t_tools_save.insert ("end", str(e_feat_maf_line1_buy.get()) + "\n")
                # 68 FEAT MA FOLLOW LINE1 SELL
                t_tools_save.insert ("end", str(e_feat_maf_line1_sell.get()) + "\n")
                # 69 FEAT MA FOLLOW LINE2 PRO
                t_tools_save.insert ("end", str(e_feat_maf_line2_pro.get()) + "\n")
                # 70 FEAT MA FOLLOW LINE2 BUY
                t_tools_save.insert ("end", str(e_feat_maf_line2_buy.get()) + "\n")
                # 71 FEAT MA FOLLOW LINE2 SELL
                t_tools_save.insert ("end", str(e_feat_maf_line2_sell.get()) + "\n")
                # 72 FEAT MA FOLLOW LINE3 PRO
                t_tools_save.insert ("end", str(e_feat_maf_line3_pro.get()) + "\n")
                # 73 FEAT MA FOLLOW LINE3 BUY
                t_tools_save.insert ("end", str(e_feat_maf_line3_buy.get()) + "\n")
                # 74 FEAT MA FOLLOW LINE3 SELL
                t_tools_save.insert ("end", str(e_feat_maf_line3_sell.get()) + "\n")
                # 75 FEAT MA FOLLOW LINE4 PRO
                t_tools_save.insert ("end", str(e_feat_maf_line4_pro.get()) + "\n")
                # 76 FEAT MA FOLLOW LINE4 BUY
                t_tools_save.insert ("end", str(e_feat_maf_line4_buy.get()) + "\n")
                # 77 FEAT MA FOLLOW LINE4 SELL
                t_tools_save.insert ("end", str(e_feat_maf_line4_sell.get()) + "\n")
                # 78 FEAT MA FOLLOW LINE5 PRO
                t_tools_save.insert ("end", str(e_feat_maf_line5_pro.get()) + "\n")
                # 79 FEAT MA FOLLOW LINE5 BUY
                t_tools_save.insert ("end", str(e_feat_maf_line5_buy.get()) + "\n")
                # 80 FEAT MA FOLLOW LINE5 SELL
                t_tools_save.insert ("end", str(e_feat_maf_line5_sell.get()) + "\n")
                # 81 FEAT MA FOLLOW LINE6 PRO
                t_tools_save.insert ("end", str(e_feat_maf_line6_pro.get()) + "\n")
                # 82 FEAT MA FOLLOW LINE6 BUY
                t_tools_save.insert ("end", str(e_feat_maf_line6_buy.get()) + "\n")
                # 83 FEAT MA FOLLOW LINE6 SELL
                t_tools_save.insert ("end", str(e_feat_maf_line6_sell.get()) + "\n")
                # 84 FEAT MA FOLLOW LINE7 PRO
                t_tools_save.insert ("end", str(e_feat_maf_line7_pro.get()) + "\n")
                # 85 FEAT MA FOLLOW LINE7 BUY
                t_tools_save.insert ("end", str(e_feat_maf_line7_buy.get()) + "\n")
                # 86 FEAT MA FOLLOW LINE7 SELL
                t_tools_save.insert ("end", str(e_feat_maf_line7_sell.get()) + "\n")




            class para_in_thread(Thread):
                def run(self):
                    try:

                        # 1 PAIR
                        e_pair.delete (0,"end")
                        e_pair.insert (0, t_tools_save.get("1.0", "1.end"))
                        # 2 Intervall sec
                        e_sec_intervall.delete (0,"end")
                        e_sec_intervall.insert (0, t_tools_save.get("2.0", "2.end"))
                        # 3 Main Amount komma
                        b_main_am_k.configure (text=t_tools_save.get("3.0", "3.end"))
                        # 4 Main Buy Amount
                        e_main_amount_buy.delete (0,"end")
                        e_main_amount_buy.insert (0, t_tools_save.get("4.0", "4.end"))
                        # 5 Main Buy onoff
                        b_main_buy_onoff.configure (bg=t_tools_save.get("5.0", "5.end"))
                        # 6 Main Buy price
                        e_main_price_buy.delete (0,"end")
                        e_main_price_buy.insert (0, t_tools_save.get("6.0", "6.end"))
                        # 7 Main Buy prozente
                        e_main_pro_buy.delete (0,"end")
                        e_main_pro_buy.insert (0, t_tools_save.get("7.0", "7.end"))
                        # 8 Main BP
                        e_main_bp.delete (0,"end")
                        e_main_bp.insert (0, t_tools_save.get("8.0", "8.end"))
                        # 9 Main BP komma
                        b_main_bp_k.configure (text=t_tools_save.get("9.0", "9.end"))
                        # 10 Main Sell Amount
                        e_main_amount_sell.delete (0,"end")
                        e_main_amount_sell.insert (0, t_tools_save.get("10.0", "10.end"))
                        # 11 Main Sell onoff
                        b_main_sell_onoff.configure (bg=t_tools_save.get("11.0", "11.end"))
                        # 12 Main Sell price
                        e_main_price_sell.delete (0,"end")
                        e_main_price_sell.insert (0, t_tools_save.get("12.0", "12.end"))
                        # 13 Main Sell prozente
                        e_main_pro_sell.delete (0,"end")
                        e_main_pro_sell.insert (0, t_tools_save.get("13.0", "13.end"))
                        # 14 Funds A2 Amount
                        e_funds_a2.delete (0,"end")
                        e_funds_a2.insert (0, t_tools_save.get("14.0", "14.end"))
                        # 15 Funds A2 komma
                        b_funds_a2_k.configure (text=t_tools_save.get("15.0", "15.end"))
                        # 16 Funds A1 Amount
                        e_funds_a1.delete (0,"end")
                        e_funds_a1.insert (0, t_tools_save.get("16.0", "16.end"))
                        # 17 Funds A1 komma
                        b_funds_a1_k.configure (text=t_tools_save.get("17.0", "17.end"))
                        # 18 Counter buy
                        e_counter_buy.delete (0,"end")
                        e_counter_buy.insert (0, t_tools_save.get("18.0", "18.end"))
                        # 19 Counter gesamt
                        e_counter_gesamt.delete (0,"end")
                        e_counter_gesamt.insert (0, t_tools_save.get("19.0", "19.end"))
                        # 20 Counter sell
                        e_counter_sell.delete (0,"end")
                        e_counter_sell.insert (0, t_tools_save.get("20.0", "20.end"))
                        # 21 Fees
                        e_main_fees.delete (0,"end")
                        e_main_fees.insert (0, t_tools_save.get("21.0", "21.end"))
                        # 22 FEAT FUNDS CONTROL 1  ONOFF
                        b_feat_fcon_onoff1.configure (bg=t_tools_save.get("22.0", "22.end"))
                        # 23 FEAT FUNDS CONTROL 1  ASSET
                        b_feat_fcon_asset1.configure (text=t_tools_save.get("23.0", "23.end"))
                        # 24 FEAT FUNDS CONTROL 1  OVER/UNDER
                        b_feat_fcon_over1.configure (text=t_tools_save.get("24.0", "24.end"))
                        # 25 FEAT FUNDS CONTROL 1  BETRAG
                        e_feat_fcon_funds1.delete (0,"end")
                        e_feat_fcon_funds1.insert (0, t_tools_save.get("25.0", "25.end"))
                        # 26 FEAT FUNDS CONTROL 1  START/STOP
                        b_feat_fcon_start1.configure (text=t_tools_save.get("26.0", "26.end"))
                        # 27 FEAT FUNDS CONTROL 1  TRADE
                        b_feat_fcon_trade1.configure (text=t_tools_save.get("27.0", "27.end"))
                        # 28 SIM ONOFF
                        b_bot_sim_onoff.configure (bg=t_tools_save.get("28.0", "28.end"))
                        # 29 DOCU ONOFF
                        b_bot_docu_onoff.configure (bg=t_tools_save.get("29.0", "29.end"))
                        # 30 FEAT PRICE CONTROL ONOFF
                        b_feat_pcon_onoff.configure (bg=t_tools_save.get("30.0", "30.end"))
                        # 31 FEAT PRICE CONTROL UNDER PRICE
                        e_feat_pcon_u_price.delete (0,"end")
                        e_feat_pcon_u_price.insert (0, t_tools_save.get("31.0", "31.end"))
                        # 32 FEAT PRICE CONTROL UNDER BUY
                        b_feat_pcon_u_buy.configure (bg=t_tools_save.get("32.0", "32.end"))
                        # 33 FEAT PRICE CONTROL UNDER SELL
                        b_feat_pcon_u_sell.configure (bg=t_tools_save.get("33.0", "33.end"))
                        # 34 FEAT PRICE CONTROL UNDER ELSE ONOFF
                        b_feat_pcon_u_e_onoff.configure (bg=t_tools_save.get("34.0", "34.end"))
                        # 35 FEAT PRICE CONTROL UNDER ELSE BUY
                        b_feat_pcon_u_e_buy.configure (bg=t_tools_save.get("35.0", "35.end"))
                        # 36 FEAT PRICE CONTROL UNDER ELSE SELL
                        b_feat_pcon_u_e_sell.configure (bg=t_tools_save.get("36.0", "36.end"))
                        # 37 FEAT PRICE CONTROL OVER PRICE
                        e_feat_pcon_o_price.delete (0,"end")
                        e_feat_pcon_o_price.insert (0, t_tools_save.get("37.0", "37.end"))
                        # 38 FEAT PRICE CONTROL OVER BUY
                        b_feat_pcon_o_buy.configure (bg=t_tools_save.get("38.0", "38.end"))
                        # 39 FEAT PRICE CONTROL OVER SELL
                        b_feat_pcon_o_sell.configure (bg=t_tools_save.get("39.0", "39.end"))
                        # 40 FEAT PRICE CONTROL OVER ELSE ONOFF
                        b_feat_pcon_o_e_onoff.configure (bg=t_tools_save.get("40.0", "40.end"))
                        # 41 FEAT PRICE CONTROL OVER ELSE BUY
                        b_feat_pcon_o_e_buy.configure (bg=t_tools_save.get("41.0", "41.end"))
                        # 42 FEAT PRICE CONTROL OVER ELSE SELL
                        b_feat_pcon_o_e_sell.configure (bg=t_tools_save.get("42.0", "42.end"))
                        # 43 Main Buy price 2
                        e_main_price_buy2.delete (0,"end")
                        e_main_price_buy2.insert (0, t_tools_save.get("43.0", "43.end"))
                        # 44 Main Buy price 3
                        e_main_price_buy3.delete (0,"end")
                        e_main_price_buy3.insert (0, t_tools_save.get("44.0", "44.end"))
                        # 45 Main Sell price 2
                        e_main_price_sell2.delete (0,"end")
                        e_main_price_sell2.insert (0, t_tools_save.get("45.0", "45.end"))
                        # 46 Main Sell price 3
                        e_main_price_sell3.delete (0,"end")
                        e_main_price_sell3.insert (0, t_tools_save.get("46.0", "46.end"))
                        # 47 Price Buy onoff 1
                        b_main_price_buy_onoff.configure (bg=t_tools_save.get("47.0", "47.end"))
                        # 48 Price Buy onoff 2
                        b_main_price_buy2_onoff.configure (bg=t_tools_save.get("48.0", "48.end"))
                        # 49 Price Buy onoff 3
                        b_main_price_buy3_onoff.configure (bg=t_tools_save.get("49.0", "49.end"))
                        # 50 Price Sell onoff 1
                        b_main_price_sell_onoff.configure (bg=t_tools_save.get("50.0", "50.end"))
                        # 51 Price Sell onoff 2
                        b_main_price_sell2_onoff.configure (bg=t_tools_save.get("51.0", "51.end"))
                        # 52 Price Sell onoff 3
                        b_main_price_sell3_onoff.configure (bg=t_tools_save.get("52.0", "52.end"))
                        # 53 Main Buy price 4
                        e_main_price_buy4.delete (0,"end")
                        e_main_price_buy4.insert (0, t_tools_save.get("53.0", "53.end"))
                        # 54 Main Buy price 5
                        e_main_price_buy5.delete (0,"end")
                        e_main_price_buy5.insert (0, t_tools_save.get("54.0", "54.end"))
                        # 55 Main sell price 4
                        e_main_price_sell4.delete (0,"end")
                        e_main_price_sell4.insert (0, t_tools_save.get("55.0", "55.end"))
                        # 56 Main sell price 5
                        e_main_price_sell5.delete (0,"end")
                        e_main_price_sell5.insert (0, t_tools_save.get("56.0", "56.end"))
                        # 57 Price Buy onoff 4
                        b_main_price_buy4_onoff.configure (bg=t_tools_save.get("57.0", "57.end"))
                        # 58 Price Buy onoff 5
                        b_main_price_buy5_onoff.configure (bg=t_tools_save.get("58.0", "58.end"))
                        # 59 Price sell onoff 4
                        b_main_price_sell4_onoff.configure (bg=t_tools_save.get("59.0", "59.end"))
                        # 60 Price sell onoff 5
                        b_main_price_sell5_onoff.configure (bg=t_tools_save.get("60.0", "60.end"))
                        # 61 FEAT MA FOLLOW ONOFF
                        b_feat_maf_onoff.configure (bg=t_tools_save.get("61.0", "61.end"))
                        # 62 FEAT MA FOLLOW INTERVALL
                        b_feat_maf_interval.configure (text=t_tools_save.get("62.0", "62.end"))
                        # 63 FEAT MA FOLLOW LIMIT
                        e_feat_maf_limit.delete (0,"end")
                        e_feat_maf_limit.insert (0, t_tools_save.get("63.0", "63.end"))
                        # 64 FEAT MA FOLLOW KOMMA
                        b_feat_maf_k.configure (text=t_tools_save.get("64.0", "64.end"))
                        # 65 FEAT MA FOLLOW ROUND
                        e_feat_maf_round.delete (0,"end")
                        e_feat_maf_round.insert (0, t_tools_save.get("65.0", "65.end"))
                        # 66 FEAT MA FOLLOW LINE1 PRO
                        e_feat_maf_line1_pro.delete (0,"end")
                        e_feat_maf_line1_pro.insert (0, t_tools_save.get("66.0", "66.end"))
                        # 67 FEAT MA FOLLOW LINE1 BUY
                        e_feat_maf_line1_buy.delete (0,"end")
                        e_feat_maf_line1_buy.insert (0, t_tools_save.get("67.0", "67.end"))
                        # 68 FEAT MA FOLLOW LINE1 SELL
                        e_feat_maf_line1_sell.delete (0,"end")
                        e_feat_maf_line1_sell.insert (0, t_tools_save.get("68.0", "68.end"))
                        # 69 FEAT MA FOLLOW LINE2 PRO
                        e_feat_maf_line2_pro.delete (0,"end")
                        e_feat_maf_line2_pro.insert (0, t_tools_save.get("69.0", "69.end"))
                        # 70 FEAT MA FOLLOW LINE2 BUY
                        e_feat_maf_line2_buy.delete (0,"end")
                        e_feat_maf_line2_buy.insert (0, t_tools_save.get("70.0", "70.end"))
                        # 71 FEAT MA FOLLOW LINE2 SELL
                        e_feat_maf_line2_sell.delete (0,"end")
                        e_feat_maf_line2_sell.insert (0, t_tools_save.get("71.0", "71.end"))
                        # 72 FEAT MA FOLLOW LINE3 PRO
                        e_feat_maf_line3_pro.delete (0,"end")
                        e_feat_maf_line3_pro.insert (0, t_tools_save.get("72.0", "72.end"))
                        # 73 FEAT MA FOLLOW LINE3 BUY
                        e_feat_maf_line3_buy.delete (0,"end")
                        e_feat_maf_line3_buy.insert (0, t_tools_save.get("73.0", "73.end"))
                        # 74 FEAT MA FOLLOW LINE3 SELL
                        e_feat_maf_line3_sell.delete (0,"end")
                        e_feat_maf_line3_sell.insert (0, t_tools_save.get("74.0", "74.end"))
                        # 75 FEAT MA FOLLOW LINE4 PRO
                        e_feat_maf_line4_pro.delete (0,"end")
                        e_feat_maf_line4_pro.insert (0, t_tools_save.get("75.0", "75.end"))
                        # 76 FEAT MA FOLLOW LINE4 BUY
                        e_feat_maf_line4_buy.delete (0,"end")
                        e_feat_maf_line4_buy.insert (0, t_tools_save.get("76.0", "76.end"))
                        # 77 FEAT MA FOLLOW LINE4 SELL
                        e_feat_maf_line4_sell.delete (0,"end")
                        e_feat_maf_line4_sell.insert (0, t_tools_save.get("77.0", "77.end"))
                        # 78 FEAT MA FOLLOW LINE5 PRO
                        e_feat_maf_line5_pro.delete (0,"end")
                        e_feat_maf_line5_pro.insert (0, t_tools_save.get("78.0", "78.end"))
                        # 79 FEAT MA FOLLOW LINE5 BUY
                        e_feat_maf_line5_buy.delete (0,"end")
                        e_feat_maf_line5_buy.insert (0, t_tools_save.get("79.0", "79.end"))
                        # 80 FEAT MA FOLLOW LINE5 SELL
                        e_feat_maf_line5_sell.delete (0,"end")
                        e_feat_maf_line5_sell.insert (0, t_tools_save.get("80.0", "80.end"))
                        # 81 FEAT MA FOLLOW LINE6 PRO
                        e_feat_maf_line6_pro.delete (0,"end")
                        e_feat_maf_line6_pro.insert (0, t_tools_save.get("81.0", "81.end"))
                        # 82 FEAT MA FOLLOW LINE6 BUY
                        e_feat_maf_line6_buy.delete (0,"end")
                        e_feat_maf_line6_buy.insert (0, t_tools_save.get("82.0", "82.end"))
                        # 83 FEAT MA FOLLOW LINE6 SELL
                        e_feat_maf_line6_sell.delete (0,"end")
                        e_feat_maf_line6_sell.insert (0, t_tools_save.get("83.0", "83.end"))
                        # 81 FEAT MA FOLLOW LINE7 PRO
                        e_feat_maf_line7_pro.delete (0,"end")
                        e_feat_maf_line7_pro.insert (0, t_tools_save.get("84.0", "84.end"))
                        # 82 FEAT MA FOLLOW LINE7 BUY
                        e_feat_maf_line7_buy.delete (0,"end")
                        e_feat_maf_line7_buy.insert (0, t_tools_save.get("85.0", "85.end"))
                        # 83 FEAT MA FOLLOW LINE7 SELL
                        e_feat_maf_line7_sell.delete (0,"end")
                        e_feat_maf_line7_sell.insert (0, t_tools_save.get("86.0", "86.end"))




                    except:
                        pass

        
            def para_in():
                para_in_thread().start()


            def safu_save():
                safu = open ("log/bot1/save_" + b_nbot_template.cget ("text") + ".txt" , "w")
                safu.write ( t_tools_save.get("1.0", "end"))
                safu.close()

            def safu_load():
                try:
                    safu = open ("log/bot1/save_" + b_nbot_template.cget ("text") + ".txt" , "r")
                    paras = safu.readlines()
                    safu.close()
                    inhalt = "".join (paras)
                    t_tools_save.delete ("1.0", "end")
                    t_tools_save.insert ("1.0", inhalt)
                except:
                    pass

            # Autosave
            if 1==1:
                class autosave_thread(Thread):
                    def run(self):
                        try:
                            para_out()

                            safu = open ("log/bot1/asave_" + b_nbot_template.cget ("text") + ".txt" , "w")
                            safu.write ( t_tools_save.get("1.0", "end"))
                            safu.close()
                        except:
                            pass

            b_tools_para_out = tk.Button(f, text="Out", command=para_out)
            b_tools_para_out.place(x=coord_x, y=coord_y - 5, width=50, height=20)

            b_tools_save = tk.Button(f, text="Save", command=safu_save)
            b_tools_save.place(x=coord_x, y=coord_y + 20, width=50, height=20)

            b_tools_load = tk.Button(f, text="Load", command=safu_load)
            b_tools_load.place(x=coord_x + 60, y=coord_y - 5, width=50, height=20)
            
            b_tools_para_in = tk.Button(f, text="In", command=para_in)
            b_tools_para_in.place(x=coord_x + 60, y=coord_y + 20, width=50, height=20)

            # Templates und Keys
            def nbot_template():
                global template_nr
                try:
                    save_file = open ("log/bot1/template.txt").read()

                    t_save.delete ("1.0", "end")
                    t_save.insert ("1.0", save_file)
                    
                except Exception as e:
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <LOAD FILE FAIL>\nEXCEPTION: " + str(e) + "\n\n")
                    return

                if template_nr == 0:
                    template_nr = 1
                    b_nbot_template.configure (text=t_save.get ("1.0", "1.end"))
                elif template_nr == 1:
                    template_nr = 2
                    b_nbot_template.configure (text=t_save.get ("2.0", "2.end"))
                elif template_nr == 2:
                    template_nr = 3
                    b_nbot_template.configure (text=t_save.get ("3.0", "3.end"))
                elif template_nr == 3:
                    template_nr = 4
                    b_nbot_template.configure (text=t_save.get ("4.0", "4.end"))
                elif template_nr == 4:
                    template_nr = 5
                    b_nbot_template.configure (text=t_save.get ("5.0", "5.end"))
                elif template_nr == 5:
                    template_nr = 6
                    b_nbot_template.configure (text=t_save.get ("6.0", "6.end"))
                elif template_nr == 6:
                    template_nr = 7
                    b_nbot_template.configure (text=t_save.get ("7.0", "7.end"))
                elif template_nr == 7:
                    template_nr = 8
                    b_nbot_template.configure (text=t_save.get ("8.0", "8.end"))
                elif template_nr == 8:
                    template_nr = 9
                    b_nbot_template.configure (text=t_save.get ("9.0", "9.end"))
                elif template_nr == 9:
                    template_nr = 10
                    b_nbot_template.configure (text=t_save.get ("10.0", "10.end"))
                elif template_nr == 10:
                    template_nr = 0
                    b_nbot_template.configure (text="0")

                if b_bot_sim_onoff.cget ("bg") == gruen:
                   b_nbot_template.configure (text="S_" + str(b_nbot_template.cget ("text")))



            b_nbot_template = tk.Button (f, font=('Courier New', 12, 'bold'), text="0", bg="#99FFCC", command=nbot_template)
            b_nbot_template.place(x=coord_x, y=coord_y + 45, width=110, height=18)

            #b_nbot_keys = tk.Button (f, font=('Courier New', 12, 'bold'), text=1, bg="#99FFCC", command=nbot_keys)
            #b_nbot_keys.place(x=coord_x + 115, y=coord_y + 45, width=20, height=18)


            t_tools_save = tk.Text (f, font=('Courier New', 9, 'bold'))
            t_tools_save.place(x=coord_x, y=coord_y - 150, width="135", height="130")

            # Temp Textfield für Templates
            t_save = tk.Text (f)

# MAIN FELD (gelbes Feld)
if 1==1:
    # Hintergrund
    area_bot = tk.Label (f,relief="ridge", bg="#EEE8AA")
    area_bot.place (x=680, y=10, width=750, height=590)

    # Main System
    if 1==1:
        coord_x = 880
        coord_y = 140

        # fees
        l_main_fees = tk.Label (f, text="Fee",  font=('Courier New', 16, 'bold'), bg="#EEE8AA")
        l_main_fees.place (x=coord_x + 390, y=coord_y - 35, width=45, height=25)

        e_main_fees = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_fees.place (x=coord_x + 440, y=coord_y - 35, width=100, height=25)
        e_main_fees.insert (0, 0.075)

        # buy
        def main_am_k():
            if b_main_am_k.cget ("text") == "%.0f":
                b_main_am_k.configure (text="%.1f")
            elif b_main_am_k.cget ("text") == "%.1f":
                b_main_am_k.configure (text="%.2f")
            elif b_main_am_k.cget ("text") == "%.2f":
                b_main_am_k.configure (text="%.3f")
            elif b_main_am_k.cget ("text") == "%.3f":
                b_main_am_k.configure (text="%.4f")
            elif b_main_am_k.cget ("text") == "%.4f":
                b_main_am_k.configure (text="%.5f")
            elif b_main_am_k.cget ("text") == "%.5f":
                b_main_am_k.configure (text="%.6f")
            elif b_main_am_k.cget ("text") == "%.6f":
                b_main_am_k.configure (text="%.7f")
            elif b_main_am_k.cget ("text") == "%.7f":
                b_main_am_k.configure (text="%.8f")
            elif b_main_am_k.cget ("text") == "%.8f":
                b_main_am_k.configure (text="%.0f")
        b_main_am_k = tk.Button(f, text="%.2f", font=('Courier New', 14, 'bold'), command=main_am_k)
        b_main_am_k.place (x=coord_x - 50, y=coord_y, width=45, height=25)
        
        e_main_amount_buy = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_amount_buy.place (x=coord_x, y=coord_y, width=100, height=25)
        e_main_amount_buy.insert (0, "0.00")
        
        def main_buy_onoff():
            if b_main_buy_onoff.cget ("bg") == rot:
                b_main_buy_onoff.configure (bg=gruen)
            elif b_main_buy_onoff.cget ("bg") == gruen:
                b_main_buy_onoff.configure (bg=rot)
        b_main_buy_onoff = tk.Button(f, text="B", font=('Courier New', 18, 'bold'), bg=gruen, command=main_buy_onoff)
        b_main_buy_onoff.place (x=coord_x + 105, y=coord_y, width=25, height=25)
        
        e_main_price_buy = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_buy.place (x=coord_x + 135, y=coord_y, width=150, height=25)
        e_main_price_buy.insert (0, "0.00000000")
        
        def main_price_buy_onoff():
            if b_main_price_buy_onoff.cget ("bg") == rot:
                b_main_price_buy_onoff.configure (bg=gruen)
                b_main_price_buy2_onoff.configure (bg=rot)
                b_main_price_buy3_onoff.configure (bg=rot)
                b_main_price_buy4_onoff.configure (bg=rot)
                b_main_price_buy5_onoff.configure (bg=rot)
        b_main_price_buy_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=gruen, command=main_price_buy_onoff)
        b_main_price_buy_onoff.place (x=coord_x + 290, y=coord_y, width=25, height=25)

        e_main_price_buy2 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_buy2.place (x=coord_x + 135, y=coord_y - 30, width=150, height=25)
        e_main_price_buy2.insert (0, "0.00000000")

        def main_price_buy2_onoff():
            if b_main_price_buy2_onoff.cget ("bg") == rot:
                b_main_price_buy2_onoff.configure (bg=gruen)
                b_main_price_buy3_onoff.configure (bg=rot)
                b_main_price_buy4_onoff.configure (bg=rot)
                b_main_price_buy5_onoff.configure (bg=rot)
                b_main_price_buy_onoff.configure (bg=rot)
        b_main_price_buy2_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=rot, command=main_price_buy2_onoff)
        b_main_price_buy2_onoff.place (x=coord_x + 290, y=coord_y - 30, width=25, height=25)

        e_main_price_buy3 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_buy3.place (x=coord_x + 135, y=coord_y - 60, width=150, height=25)
        e_main_price_buy3.insert (0, "0.00000000")

        def main_price_buy3_onoff():
            if b_main_price_buy3_onoff.cget ("bg") == rot:
                b_main_price_buy3_onoff.configure (bg=gruen)
                b_main_price_buy_onoff.configure (bg=rot)
                b_main_price_buy2_onoff.configure (bg=rot)
                b_main_price_buy4_onoff.configure (bg=rot)
                b_main_price_buy5_onoff.configure (bg=rot)
        b_main_price_buy3_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=rot, command=main_price_buy3_onoff)
        b_main_price_buy3_onoff.place (x=coord_x + 290, y=coord_y - 60, width=25, height=25)

        e_main_price_buy4 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_buy4.place (x=coord_x + 135, y=coord_y - 90, width=150, height=25)
        e_main_price_buy4.insert (0, "0.00000000")

        def main_price_buy4_onoff():
            if b_main_price_buy4_onoff.cget ("bg") == rot:
                b_main_price_buy4_onoff.configure (bg=gruen)
                b_main_price_buy_onoff.configure (bg=rot)
                b_main_price_buy2_onoff.configure (bg=rot)
                b_main_price_buy3_onoff.configure (bg=rot)
                b_main_price_buy5_onoff.configure (bg=rot)
        b_main_price_buy4_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=rot, command=main_price_buy4_onoff)
        b_main_price_buy4_onoff.place (x=coord_x + 290, y=coord_y - 90, width=25, height=25)

        e_main_price_buy5 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_buy5.place (x=coord_x + 135, y=coord_y - 120, width=150, height=25)
        e_main_price_buy5.insert (0, "0.00000000")

        def main_price_buy5_onoff():
            if b_main_price_buy5_onoff.cget ("bg") == rot:
                b_main_price_buy5_onoff.configure (bg=gruen)
                b_main_price_buy_onoff.configure (bg=rot)
                b_main_price_buy2_onoff.configure (bg=rot)
                b_main_price_buy3_onoff.configure (bg=rot)
                b_main_price_buy4_onoff.configure (bg=rot)
        b_main_price_buy5_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=rot, command=main_price_buy5_onoff)
        b_main_price_buy5_onoff.place (x=coord_x + 290, y=coord_y - 120, width=25, height=25)


        e_main_pro_buy = tk.Entry(f, font=('Courier New', 18, 'bold'), bg=gruen)
        e_main_pro_buy.place (x=coord_x + 340, y=coord_y, width=100, height=25)
        e_main_pro_buy.insert (0, 1)


        # Basic Price
        def main_bp_cal():
            if float(e_main_bp.get()) == 0:
                return
            
            e_main_price_buy.delete (0, "end")
            e_main_price_buy.insert (0, b_main_bp_k.cget("text") % (float(e_main_bp.get()) * ((100 - float(e_main_pro_buy.get())) / 100)))

            e_main_price_buy2.delete (0, "end")
            e_main_price_buy2.insert (0, b_main_bp_k.cget("text") % (float(e_main_price_buy.get()) * ((100 - float(e_main_pro_buy.get())) / 100)))
            
            e_main_price_buy3.delete (0, "end")
            e_main_price_buy3.insert (0, b_main_bp_k.cget("text") % (float(e_main_price_buy2.get()) * ((100 - float(e_main_pro_buy.get())) / 100)))

            e_main_price_buy4.delete (0, "end")
            e_main_price_buy4.insert (0, b_main_bp_k.cget("text") % (float(e_main_price_buy3.get()) * ((100 - float(e_main_pro_buy.get())) / 100)))
            
            e_main_price_buy5.delete (0, "end")
            e_main_price_buy5.insert (0, b_main_bp_k.cget("text") % (float(e_main_price_buy4.get()) * ((100 - float(e_main_pro_buy.get())) / 100)))
            
            e_main_price_sell.delete (0, "end")
            e_main_price_sell.insert (0, b_main_bp_k.cget("text") % (float(e_main_bp.get()) * ((100 + float(e_main_pro_sell.get())) / 100)))

            e_main_price_sell2.delete (0, "end")
            e_main_price_sell2.insert (0, b_main_bp_k.cget("text") % (float(e_main_price_sell.get()) * ((100 + float(e_main_pro_sell.get())) / 100)))

            e_main_price_sell3.delete (0, "end")
            e_main_price_sell3.insert (0, b_main_bp_k.cget("text") % (float(e_main_price_sell2.get()) * ((100 + float(e_main_pro_sell.get())) / 100)))

            e_main_price_sell4.delete (0, "end")
            e_main_price_sell4.insert (0, b_main_bp_k.cget("text") % (float(e_main_price_sell3.get()) * ((100 + float(e_main_pro_sell.get())) / 100)))

            e_main_price_sell5.delete (0, "end")
            e_main_price_sell5.insert (0, b_main_bp_k.cget("text") % (float(e_main_price_sell4.get()) * ((100 + float(e_main_pro_sell.get())) / 100)))


        b_main_bp_cal = tk.Button(f, text="Cal", font=('Courier New', 16, 'bold'), command=main_bp_cal)
        b_main_bp_cal.place (x=coord_x + 55, y=coord_y + 35, width=45, height=25)
        
        def main_bp_load():
            e_main_bp.delete (0, "end")
            e_main_bp.insert (0, float(l_price.cget("text")))
        b_main_bp_load = tk.Button(f, text="L", font=('Courier New', 18, 'bold'), command=main_bp_load)
        b_main_bp_load.place (x=coord_x + 105, y=coord_y + 35, width=25, height=25)

        e_main_bp = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_bp.place (x=coord_x + 135, y=coord_y + 35, width=150, height=25)
        e_main_bp.insert (0, "0.00000000")

        def main_am_k():
            if b_main_bp_k.cget ("text") == "%.0f":
                b_main_bp_k.configure (text="%.1f")
            elif b_main_bp_k.cget ("text") == "%.1f":
                b_main_bp_k.configure (text="%.2f")
            elif b_main_bp_k.cget ("text") == "%.2f":
                b_main_bp_k.configure (text="%.3f")
            elif b_main_bp_k.cget ("text") == "%.3f":
                b_main_bp_k.configure (text="%.4f")
            elif b_main_bp_k.cget ("text") == "%.4f":
                b_main_bp_k.configure (text="%.5f")
            elif b_main_bp_k.cget ("text") == "%.5f":
                b_main_bp_k.configure (text="%.6f")
            elif b_main_bp_k.cget ("text") == "%.6f":
                b_main_bp_k.configure (text="%.7f")
            elif b_main_bp_k.cget ("text") == "%.7f":
                b_main_bp_k.configure (text="%.8f")
            elif b_main_bp_k.cget ("text") == "%.8f":
                b_main_bp_k.configure (text="%.0f")
        b_main_bp_k = tk.Button(f, text="%.2f", font=('Courier New', 14, 'bold'), command=main_am_k)
        b_main_bp_k.place (x=coord_x + 295, y=coord_y + 35, width=45, height=25)

        # sell
        coord_y += 70
        e_main_amount_sell = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_amount_sell.place (x=coord_x, y=coord_y, width=100, height=25)
        e_main_amount_sell.insert (0, "0.00")
        
        def main_sell_onoff():
            if b_main_sell_onoff.cget ("bg") == rot:
                b_main_sell_onoff.configure (bg=gruen)
            elif b_main_sell_onoff.cget ("bg") == gruen:
                b_main_sell_onoff.configure (bg=rot)
        b_main_sell_onoff = tk.Button(f, text="S", font=('Courier New', 18, 'bold'), bg=gruen, command=main_sell_onoff)
        b_main_sell_onoff.place (x=coord_x + 105, y=coord_y, width=25, height=25)
        
        e_main_price_sell = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_sell.place (x=coord_x + 135, y=coord_y, width=150, height=25)
        e_main_price_sell.insert (0, "0.00000000")
        
        def main_price_sell_onoff():
            if b_main_price_sell_onoff.cget ("bg") == rot:
                b_main_price_sell_onoff.configure (bg=gruen)
                b_main_price_sell2_onoff.configure (bg=rot)
                b_main_price_sell3_onoff.configure (bg=rot)
                b_main_price_sell4_onoff.configure (bg=rot)
                b_main_price_sell5_onoff.configure (bg=rot)
        b_main_price_sell_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=gruen, command=main_price_sell_onoff)
        b_main_price_sell_onoff.place (x=coord_x + 290, y=coord_y, width=25, height=25)

        e_main_price_sell2 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_sell2.place (x=coord_x + 135, y=coord_y + 30, width=150, height=25)
        e_main_price_sell2.insert (0, "0.00000000")

        def main_price_sell2_onoff():
            if b_main_price_sell2_onoff.cget ("bg") == rot:
                b_main_price_sell2_onoff.configure (bg=gruen)
                b_main_price_sell3_onoff.configure (bg=rot)
                b_main_price_sell_onoff.configure (bg=rot)
                b_main_price_sell4_onoff.configure (bg=rot)
                b_main_price_sell5_onoff.configure (bg=rot)
        b_main_price_sell2_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=rot, command=main_price_sell2_onoff)
        b_main_price_sell2_onoff.place (x=coord_x + 290, y=coord_y + 30, width=25, height=25)

        e_main_price_sell3 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_sell3.place (x=coord_x + 135, y=coord_y + 60, width=150, height=25)
        e_main_price_sell3.insert (0, "0.00000000")

        def main_price_sell3_onoff():
            if b_main_price_sell3_onoff.cget ("bg") == rot:
                b_main_price_sell3_onoff.configure (bg=gruen)
                b_main_price_sell_onoff.configure (bg=rot)
                b_main_price_sell2_onoff.configure (bg=rot)
                b_main_price_sell4_onoff.configure (bg=rot)
                b_main_price_sell5_onoff.configure (bg=rot)
        b_main_price_sell3_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=rot, command=main_price_sell3_onoff)
        b_main_price_sell3_onoff.place (x=coord_x + 290, y=coord_y + 60, width=25, height=25)

        e_main_price_sell4 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_sell4.place (x=coord_x + 135, y=coord_y + 90, width=150, height=25)
        e_main_price_sell4.insert (0, "0.00000000")

        def main_price_sell4_onoff():
            if b_main_price_sell4_onoff.cget ("bg") == rot:
                b_main_price_sell4_onoff.configure (bg=gruen)
                b_main_price_sell_onoff.configure (bg=rot)
                b_main_price_sell2_onoff.configure (bg=rot)
                b_main_price_sell3_onoff.configure (bg=rot)
                b_main_price_sell5_onoff.configure (bg=rot)
        b_main_price_sell4_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=rot, command=main_price_sell4_onoff)
        b_main_price_sell4_onoff.place (x=coord_x + 290, y=coord_y + 90, width=25, height=25)

        e_main_price_sell5 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_main_price_sell5.place (x=coord_x + 135, y=coord_y + 120, width=150, height=25)
        e_main_price_sell5.insert (0, "0.00000000")

        def main_price_sell5_onoff():
            if b_main_price_sell5_onoff.cget ("bg") == rot:
                b_main_price_sell5_onoff.configure (bg=gruen)
                b_main_price_sell_onoff.configure (bg=rot)
                b_main_price_sell2_onoff.configure (bg=rot)
                b_main_price_sell3_onoff.configure (bg=rot)
                b_main_price_sell4_onoff.configure (bg=rot)
        b_main_price_sell5_onoff = tk.Button(f, font=('Courier New', 18, 'bold'), bg=rot, command=main_price_sell5_onoff)
        b_main_price_sell5_onoff.place (x=coord_x + 290, y=coord_y + 120, width=25, height=25)

        e_main_pro_sell = tk.Entry(f, font=('Courier New', 18, 'bold'), bg=rot)
        e_main_pro_sell.place (x=coord_x + 340, y=coord_y, width=100, height=25)
        e_main_pro_sell.insert (0, 1)

        def main_cal_sell():
            wert = 100 / (100 - float(e_main_pro_buy.get())) * 100 - 100
            e_main_pro_sell.delete (0, "end")
            e_main_pro_sell.insert (0, "%.5f" % wert)

        b_main_cal_sell = tk.Button(f, text="Cal", font=('Courier New', 16, 'bold'), command=main_cal_sell)
        b_main_cal_sell.place (x=coord_x + 450, y=coord_y, width=45, height=25)

    # Counter
    if 1==1:
        coord_x = 690
        coord_y = 50

        e_counter_buy = tk.Entry(f, font=('Courier New', 14, 'bold'))
        e_counter_buy.place (x=coord_x, y=coord_y, width=50, height=25)
        e_counter_buy.insert (0, 0)

        e_counter_gesamt = tk.Entry(f, font=('Courier New', 14, 'bold'))
        e_counter_gesamt.place (x=coord_x, y=coord_y + 35, width=50, height=25)
        e_counter_gesamt.insert (0, 0)

        e_counter_sell = tk.Entry(f, font=('Courier New', 14, 'bold'))
        e_counter_sell.place (x=coord_x, y=coord_y + 70, width=50, height=25)
        e_counter_sell.insert (0, 0)

    # Funds
    if 1==1:
        coord_x = 690
        coord_y = 365

        # Asset 2
        l_funds_a2 = tk.Label(f, text="A2", font=('TkDefaultFont', 14, 'bold'), anchor="w", bg="#EEE8AA")
        l_funds_a2.place (x=coord_x, y=coord_y, width=35, height=25)

        e_funds_a2 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_funds_a2.place (x=coord_x + 35, y=coord_y, width=150, height=25)
        e_funds_a2.insert (0, "0.00000000")

        def funds_a2_k():
            if b_funds_a2_k.cget ("text") == "%.0f":
                b_funds_a2_k.configure (text="%.1f")
            elif b_funds_a2_k.cget ("text") == "%.1f":
                b_funds_a2_k.configure (text="%.2f")
            elif b_funds_a2_k.cget ("text") == "%.2f":
                b_funds_a2_k.configure (text="%.3f")
            elif b_funds_a2_k.cget ("text") == "%.3f":
                b_funds_a2_k.configure (text="%.4f")
            elif b_funds_a2_k.cget ("text") == "%.4f":
                b_funds_a2_k.configure (text="%.5f")
            elif b_funds_a2_k.cget ("text") == "%.5f":
                b_funds_a2_k.configure (text="%.6f")
            elif b_funds_a2_k.cget ("text") == "%.6f":
                b_funds_a2_k.configure (text="%.7f")
            elif b_funds_a2_k.cget ("text") == "%.7f":
                b_funds_a2_k.configure (text="%.8f")
            elif b_funds_a2_k.cget ("text") == "%.8f":
                b_funds_a2_k.configure (text="%.0f")
        b_funds_a2_k = tk.Button(f, text="%.2f", font=('Courier New', 14, 'bold'), command=funds_a2_k)
        b_funds_a2_k.place (x=coord_x + 195, y=coord_y, width=45, height=25)
        
        def funds_a2_onoff():
            if b_funds_a2_onoff.cget ("bg") == rot:
                b_funds_a2_onoff.configure (bg=gruen)
            elif b_funds_a2_onoff.cget ("bg") == gruen:
                b_funds_a2_onoff.configure (bg=rot)
        b_funds_a2_onoff = tk.Button(f, text="Buy", font=('Courier New', 16, 'bold'), bg=gruen, command=funds_a2_onoff)
        b_funds_a2_onoff.place (x=coord_x + 250, y=coord_y, width=55, height=25)

        l_kapi_a2 = tk.Label(f, text="0.00000000", font=('Courier New', 25, 'bold'), anchor="w")
        l_kapi_a2.place (x=coord_x + 320, y=coord_y, width=200, height=30)

        # Asset 1
        coord_y += 35
        l_funds_a1 = tk.Label(f, text="A1", font=('TkDefaultFont', 14, 'bold'), anchor="w", bg="#EEE8AA")
        l_funds_a1.place (x=coord_x, y=coord_y, width=35, height=25)

        e_funds_a1 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_funds_a1.place (x=coord_x + 35, y=coord_y, width=150, height=25)
        e_funds_a1.insert (0, "0.00000000")

        def funds_a1_k():
            if b_funds_a1_k.cget ("text") == "%.0f":
                b_funds_a1_k.configure (text="%.1f")
            elif b_funds_a1_k.cget ("text") == "%.1f":
                b_funds_a1_k.configure (text="%.2f")
            elif b_funds_a1_k.cget ("text") == "%.2f":
                b_funds_a1_k.configure (text="%.3f")
            elif b_funds_a1_k.cget ("text") == "%.3f":
                b_funds_a1_k.configure (text="%.4f")
            elif b_funds_a1_k.cget ("text") == "%.4f":
                b_funds_a1_k.configure (text="%.5f")
            elif b_funds_a1_k.cget ("text") == "%.5f":
                b_funds_a1_k.configure (text="%.6f")
            elif b_funds_a1_k.cget ("text") == "%.6f":
                b_funds_a1_k.configure (text="%.7f")
            elif b_funds_a1_k.cget ("text") == "%.7f":
                b_funds_a1_k.configure (text="%.8f")
            elif b_funds_a1_k.cget ("text") == "%.8f":
                b_funds_a1_k.configure (text="%.0f")
        b_funds_a1_k = tk.Button(f, text="%.2f", font=('Courier New', 14, 'bold'), command=funds_a1_k)
        b_funds_a1_k.place (x=coord_x + 195, y=coord_y, width=45, height=25)
        
        def funds_a1_onoff():
            if b_funds_a1_onoff.cget ("bg") == rot:
                b_funds_a1_onoff.configure (bg=gruen)
            elif b_funds_a1_onoff.cget ("bg") == gruen:
                b_funds_a1_onoff.configure (bg=rot)
        b_funds_a1_onoff = tk.Button(f, text="Sell", font=('Courier New', 16, 'bold'), bg=gruen, command=funds_a1_onoff)
        b_funds_a1_onoff.place (x=coord_x + 250, y=coord_y, width=55, height=25)

        l_kapi_a1 = tk.Label(f, text="0.00000000", font=('Courier New', 25, 'bold'), anchor="w")
        l_kapi_a1.place (x=coord_x + 320, y=coord_y, width=200, height=30)


        def funds_cal():
            if float(l_price.cget("text")) == 0:
                return

            l_kapi_a2.configure (text= b_funds_a2_k.cget("text") % (float(e_funds_a1.get()) * float(l_price.cget("text")) + float(e_funds_a2.get())))
            l_kapi_a1.configure (text= b_funds_a1_k.cget("text") % (float(e_funds_a2.get()) / float(l_price.cget("text")) + float(e_funds_a1.get())))
        b_funds_cal = tk.Button(f, text="Cal", font=('Courier New', 16, 'bold'), command=funds_cal)
        b_funds_cal.place (x=coord_x + 530, y=coord_y + 2, width=45, height=25)

        # Leader Calculation
        if 1==1:

            # BUY
            class ladder_cal_buy_thread(Thread):
                def run(self):

                    buy_price = str(e_main_price_buy.get())
                    buy_funds_a1 = str(e_funds_a1.get())
                    buy_funds_a2 = str(e_funds_a2.get())
                    buy_100pro = float(e_main_bp.get())
                    counter = 0
                    
                    while float(buy_funds_a2) > float(e_main_amount_buy.get()):

                        buy_amount_a1 = b_funds_a1_k.cget("text") % ((float(e_main_amount_buy.get()) / float(buy_price)) * (1 - float(e_main_fees.get()) / 100))
                        buy_amount_a2 = str(e_main_amount_buy.get())

                        buy_funds_a1 = b_funds_a1_k.cget("text") % (float(buy_funds_a1) + float(buy_amount_a1))
                        buy_funds_a2 = b_funds_a2_k.cget("text") % (float(buy_funds_a2) - float(buy_amount_a2))

                        buy_amount_wert = b_funds_a2_k.cget("text") % (float(buy_funds_a1) * float(buy_price))


                        buy_diff_pro = "%.2f" % ((float(buy_price) / buy_100pro * 100) - 100)
                        counter += 1

                        t_log_all.insert ("1.0", buy_amount_a1  + " " + buy_price + " " +  buy_funds_a1 + "(" +   buy_amount_wert + ")" + " " +  buy_funds_a2 + " " + buy_diff_pro + " " + str(counter) + "\n")

                        buy_price = b_main_bp_k.cget("text") % (float(buy_price) * ((100 - float(e_main_pro_buy.get())) / 100))
            

            def ladder_cal_buy():
                ladder_cal_buy_thread().start()
            b_ladder_cal_buy = tk.Button(f, text="B-Cal", font=('TkDefaultFont', 12, 'bold'), command=ladder_cal_buy)
            b_ladder_cal_buy.place (x=coord_x, y=coord_y - 60, width=50, height=20)

            # SELL
            class ladder_cal_sell_thread(Thread):
                def run(self):

                    sell_price = str(e_main_price_sell.get())
                    sell_funds_a1 = str(e_funds_a1.get())
                    sell_funds_a2 = str(e_funds_a2.get())
                    sell_amount_a1 = b_funds_a1_k.cget("text") % ((float(e_main_amount_sell.get()) / float(sell_price)))
                    sell_100pro = float(e_main_bp.get())
                    counter = 0
                    
                    
                    while float(sell_funds_a1) > float(sell_amount_a1):
                        

                        sell_amount_a1 = b_funds_a1_k.cget("text") % ((float(e_main_amount_sell.get()) / float(sell_price)))
                        sell_amount_a2 = b_funds_a2_k.cget("text") % ((float(sell_amount_a1) * float(sell_price)) * (1 - float(e_main_fees.get()) / 100))

                        sell_funds_a1 = b_funds_a1_k.cget("text") % (float(sell_funds_a1) - float(sell_amount_a1))
                        sell_funds_a2 = b_funds_a2_k.cget("text") % (float(sell_funds_a2) + float(sell_amount_a2))

                        sell_amount_wert = b_funds_a2_k.cget("text") % (float(sell_funds_a1) * float(sell_price))

                        sell_diff_pro = "%.2f" % ((float(sell_price) / sell_100pro * 100) - 100)
                        counter += 1

                        t_log_all.insert ("1.0", sell_amount_a1  + " " + sell_price + " " +  sell_funds_a1 + "(" +   sell_amount_wert + ")" + sell_funds_a2 + " " + sell_diff_pro + " " + str(counter) + "\n")

                        sell_price = b_main_bp_k.cget("text") % (float(sell_price) * ((100 + float(e_main_pro_sell.get())) / 100))

                        if counter == 450:
                            break
            

            def ladder_cal_sell():
                ladder_cal_sell_thread().start()
            b_ladder_cal_sell = tk.Button(f, text="S-Cal", font=('TkDefaultFont', 12, 'bold'), command=ladder_cal_sell)
            b_ladder_cal_sell.place (x=coord_x, y=coord_y + 30, width=50, height=20)

        # Kapital vorhanden
        def kapi_vorhanden_buy():

            if b_main_price_buy_onoff.cget ("bg") == gruen:
                if float(e_funds_a2.get()) > float(e_main_amount_buy.get()):
                    b_funds_a2_onoff.configure (bg=gruen)
                else:
                    b_funds_a2_onoff.configure (bg=rot)

            elif b_main_price_buy2_onoff.cget ("bg") == gruen:
                if float(e_funds_a2.get()) > float(e_main_amount_buy.get()) * 2:
                    b_funds_a2_onoff.configure (bg=gruen)
                else:
                    b_funds_a2_onoff.configure (bg=rot)
                    
            elif b_main_price_buy3_onoff.cget ("bg") == gruen:
                if float(e_funds_a2.get()) > float(e_main_amount_buy.get()) * 3:
                    b_funds_a2_onoff.configure (bg=gruen)
                else:
                    b_funds_a2_onoff.configure (bg=rot)

            elif b_main_price_buy4_onoff.cget ("bg") == gruen:
                if float(e_funds_a2.get()) > float(e_main_amount_buy.get()) * 4:
                    b_funds_a2_onoff.configure (bg=gruen)
                else:
                    b_funds_a2_onoff.configure (bg=rot)

            elif b_main_price_buy5_onoff.cget ("bg") == gruen:
                if float(e_funds_a2.get()) > float(e_main_amount_buy.get()) * 5:
                    b_funds_a2_onoff.configure (bg=gruen)
                else:
                    b_funds_a2_onoff.configure (bg=rot)
                        
        def kapi_vorhanden_sell():

            if b_main_price_sell_onoff.cget ("bg") == gruen:
                if float(e_funds_a1.get()) >= (float(e_main_amount_sell.get()) / float(e_main_price_sell.get())):
                    b_funds_a1_onoff.configure (bg=gruen)
                else:
                    b_funds_a1_onoff.configure (bg=rot)
            elif b_main_price_sell2_onoff.cget ("bg") == gruen:
                if float(e_funds_a1.get()) >= (float(e_main_amount_sell.get()) * 2 / float(e_main_price_sell.get())):
                    b_funds_a1_onoff.configure (bg=gruen)
                else:
                    b_funds_a1_onoff.configure (bg=rot)
            elif b_main_price_sell3_onoff.cget ("bg") == gruen:
                if float(e_funds_a1.get()) >= (float(e_main_amount_sell.get()) * 3 / float(e_main_price_sell.get())):
                    b_funds_a1_onoff.configure (bg=gruen)
                else:
                    b_funds_a1_onoff.configure (bg=rot)
            elif b_main_price_sell4_onoff.cget ("bg") == gruen:
                if float(e_funds_a1.get()) >= (float(e_main_amount_sell.get()) * 4 / float(e_main_price_sell.get())):
                    b_funds_a1_onoff.configure (bg=gruen)
                else:
                    b_funds_a1_onoff.configure (bg=rot)
            elif b_main_price_sell5_onoff.cget ("bg") == gruen:
                if float(e_funds_a1.get()) >= (float(e_main_amount_sell.get()) * 5 / float(e_main_price_sell.get())):
                    b_funds_a1_onoff.configure (bg=gruen)
                else:
                    b_funds_a1_onoff.configure (bg=rot)

    # FEAT FUNDS CONTROL
    if 1==1:
        coord_x = 695
        coord_y = 460

        # Number 1
        def feat_fcon_onoff1():
            if b_feat_fcon_onoff1.cget ("bg") == rot:
                b_feat_fcon_onoff1.configure (bg=gruen)
            elif b_feat_fcon_onoff1.cget ("bg") == gruen:
                b_feat_fcon_onoff1.configure (bg=rot)
        b_feat_fcon_onoff1 = tk.Button(f, font=('Courier New', 16, 'bold'), bg=rot, command=feat_fcon_onoff1)
        b_feat_fcon_onoff1.place (x=coord_x, y=coord_y, width=20, height=25)

        def feat_fcon_asset1():
            if b_feat_fcon_asset1.cget ("text") == "A1":
                b_feat_fcon_asset1.configure (text="A2")
            elif b_feat_fcon_asset1.cget ("text") == "A2":
                b_feat_fcon_asset1.configure (text="A1")
        b_feat_fcon_asset1 = tk.Button(f, text="A1", font=('TkDefaultFont', 12, 'bold'), command=feat_fcon_asset1)
        b_feat_fcon_asset1.place (x=coord_x + 30, y=coord_y, width=40, height=25)


        def feat_fcon_over1():
            if b_feat_fcon_over1.cget ("text") == "over":
                b_feat_fcon_over1.configure (text="under")
            elif b_feat_fcon_over1.cget ("text") == "under":
                b_feat_fcon_over1.configure (text="over")
        b_feat_fcon_over1 = tk.Button(f, text="over", font=('TkDefaultFont', 12, 'bold'), command=feat_fcon_over1)
        b_feat_fcon_over1.place (x=coord_x + 75, y=coord_y, width=55, height=25)

        e_feat_fcon_funds1 = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_feat_fcon_funds1.place (x=coord_x + 135, y=coord_y, width=150, height=25)
        e_feat_fcon_funds1.insert (0, "0.00000000")

        def feat_fcon_start1():
            if b_feat_fcon_start1.cget ("text") == "start":
                b_feat_fcon_start1.configure (text="stop")
            elif b_feat_fcon_start1.cget ("text") == "stop":
                b_feat_fcon_start1.configure (text="start")
        b_feat_fcon_start1 = tk.Button(f, text="start", font=('TkDefaultFont', 12, 'bold'), command=feat_fcon_start1)
        b_feat_fcon_start1.place (x=coord_x + 295, y=coord_y, width=55, height=25)

        def feat_fcon_trade1():
            if b_feat_fcon_trade1.cget ("text") == "buy":
                b_feat_fcon_trade1.configure (text="sell")
            elif b_feat_fcon_trade1.cget ("text") == "sell":
                b_feat_fcon_trade1.configure (text="buy")
        b_feat_fcon_trade1 = tk.Button(f, text="buy", font=('TkDefaultFont', 12, 'bold'), command=feat_fcon_trade1)
        b_feat_fcon_trade1.place (x=coord_x + 355, y=coord_y, width=45, height=25)

        def feat_fcon_buy1():
            if b_feat_fcon_buy1.cget ("bg") == gruen:
                b_feat_fcon_buy1.configure (bg=rot)
            elif b_feat_fcon_buy1.cget ("bg") == rot:
                b_feat_fcon_buy1.configure (bg=gruen)
        b_feat_fcon_buy1 = tk.Button(f, text="BUY", font=('TkDefaultFont', 12, 'bold'), bg=gruen, command=feat_fcon_buy1)
        b_feat_fcon_buy1.place (x=coord_x + 415, y=coord_y, width=55, height=25)

        def feat_fcon_sell1():
            if b_feat_fcon_sell1.cget ("bg") == gruen:
                b_feat_fcon_sell1.configure (bg=rot)
            elif b_feat_fcon_sell1.cget ("bg") == rot:
                b_feat_fcon_sell1.configure (bg=gruen)
        b_feat_fcon_sell1 = tk.Button(f, text="SELL", font=('TkDefaultFont', 12, 'bold'), bg=gruen, command=feat_fcon_sell1)
        b_feat_fcon_sell1.place (x=coord_x + 480, y=coord_y, width=55, height=25)

        def feat_fcon_cal1():

            # Baum A1
            if b_feat_fcon_asset1.cget("text") == "A1":

                # Wenn Funds über ist
                if b_feat_fcon_over1.cget("text") == "over":
                    
                    # Wenn Funds über wahr ist
                    if float(e_funds_a1.get())  > float(e_feat_fcon_funds1.get()):
                        
                        # Wenn Start aktiv
                        if b_feat_fcon_start1.cget("text") == "start":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)

                        # Wenn Stop aktiv
                        elif b_feat_fcon_start1.cget("text") == "stop":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=rot)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=rot)

                    # Wenn Funds über falsch ist
                    elif float(e_funds_a1.get()) < float(e_feat_fcon_funds1.get()):

                        # Wenn Start aktiv
                        if b_feat_fcon_start1.cget("text") == "start":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=rot)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=rot)

                        # Wenn Stop aktiv
                        elif b_feat_fcon_start1.cget("text") == "stop":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)

                # Wenn Funds unter ist
                elif b_feat_fcon_over1.cget("text") == "under":
                    
                    # Wenn Funds unter wahr ist
                    if float(e_funds_a1.get())  < float(e_feat_fcon_funds1.get()):
                        
                        # Wenn Start aktiv
                        if b_feat_fcon_start1.cget("text") == "start":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)

                        # Wenn Stop aktiv
                        elif b_feat_fcon_start1.cget("text") == "stop":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=rot)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=rot)

                    # Wenn Funds unter falsch ist
                    elif float(e_funds_a1.get()) > float(e_feat_fcon_funds1.get()):

                        # Wenn Start aktiv
                        if b_feat_fcon_start1.cget("text") == "start":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=rot)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=rot)

                        # Wenn Stop aktiv
                        elif b_feat_fcon_start1.cget("text") == "stop":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)

            # Baum A2
            elif b_feat_fcon_asset1.cget("text") == "A2":

                # Wenn Funds über ist
                if b_feat_fcon_over1.cget("text") == "over":
                    
                    # Wenn Funds über wahr ist
                    if float(e_funds_a2.get())  > float(e_feat_fcon_funds1.get()):
                        
                        # Wenn Start aktiv
                        if b_feat_fcon_start1.cget("text") == "start":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)

                        # Wenn Stop aktiv
                        elif b_feat_fcon_start1.cget("text") == "stop":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=rot)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=rot)

                    # Wenn Funds über falsch ist
                    elif float(e_funds_a2.get()) < float(e_feat_fcon_funds1.get()):

                        # Wenn Start aktiv
                        if b_feat_fcon_start1.cget("text") == "start":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=rot)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=rot)

                        # Wenn Stop aktiv
                        elif b_feat_fcon_start1.cget("text") == "stop":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)

                # Wenn Funds unter ist
                elif b_feat_fcon_over1.cget("text") == "under":
                    
                    # Wenn Funds unter wahr ist
                    if float(e_funds_a2.get())  < float(e_feat_fcon_funds1.get()):
                        
                        # Wenn Start aktiv
                        if b_feat_fcon_start1.cget("text") == "start":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)

                        # Wenn Stop aktiv
                        elif b_feat_fcon_start1.cget("text") == "stop":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=rot)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=rot)

                    # Wenn Funds unter falsch ist
                    elif float(e_funds_a2.get()) > float(e_feat_fcon_funds1.get()):

                        # Wenn Start aktiv
                        if b_feat_fcon_start1.cget("text") == "start":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=rot)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=rot)

                        # Wenn Stop aktiv
                        elif b_feat_fcon_start1.cget("text") == "stop":

                            # Wenn Buy aktiv
                            if b_feat_fcon_trade1.cget("text") == "buy":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
                            # Wenn Sell aktiv
                            elif b_feat_fcon_trade1.cget("text") == "sell":
                                b_feat_fcon_buy1.configure (bg=gruen)
                                b_feat_fcon_sell1.configure (bg=gruen)
        b_feat_fcon_cal1 = tk.Button(f, text="Cal", font=('Courier New', 16, 'bold'), command=feat_fcon_cal1)
        b_feat_fcon_cal1.place (x=coord_x + 550, y=coord_y, width=45, height=25)

    # FEAT PRICE CONTROL
    if 1==1:
        coord_x = 695
        coord_y = 500

        def feat_pcon_onoff():
            if b_feat_pcon_onoff.cget ("bg") == rot:
                b_feat_pcon_onoff.configure (bg=gruen)
            elif b_feat_pcon_onoff.cget ("bg") == gruen:
                b_feat_pcon_onoff.configure (bg=rot)
        b_feat_pcon_onoff = tk.Button(f, font=('Courier New', 16, 'bold'), bg=rot, command=feat_pcon_onoff)
        b_feat_pcon_onoff.place (x=coord_x, y=coord_y, width=20, height=25)

        # UNDER
        l_feat_pcon_under = tk.Label(f, text="UNDER", font=('TkDefaultFont', 12, 'bold'), bg="#EEE8AA")
        l_feat_pcon_under.place (x=coord_x + 30, y=coord_y, width=60, height=25)

        e_feat_pcon_u_price = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_feat_pcon_u_price.place (x=coord_x + 100, y=coord_y, width=150, height=25)
        e_feat_pcon_u_price.insert (0, "0.00000000")

        def feat_pcon_u_buy():
            if b_feat_pcon_u_buy.cget ("bg") == gruen:
                b_feat_pcon_u_buy.configure (bg=rot)
            elif b_feat_pcon_u_buy.cget ("bg") == rot:
                b_feat_pcon_u_buy.configure (bg=gruen)
        b_feat_pcon_u_buy = tk.Button(f, text="BUY", font=('TkDefaultFont', 11, 'bold'), bg=gruen, command=feat_pcon_u_buy)
        b_feat_pcon_u_buy.place (x=coord_x + 260, y=coord_y, width=55, height=20)

        def feat_pcon_u_sell():
            if b_feat_pcon_u_sell.cget ("bg") == gruen:
                b_feat_pcon_u_sell.configure (bg=rot)
            elif b_feat_pcon_u_sell.cget ("bg") == rot:
                b_feat_pcon_u_sell.configure (bg=gruen)
        b_feat_pcon_u_sell = tk.Button(f, text="SELL", font=('TkDefaultFont', 11, 'bold'), bg=gruen, command=feat_pcon_u_sell)
        b_feat_pcon_u_sell.place (x=coord_x + 325, y=coord_y, width=55, height=20)

        l_feat_pcon_else_under = tk.Label(f, text="ELSE", font=('TkDefaultFont', 12, 'bold'), bg="#EEE8AA")
        l_feat_pcon_else_under.place (x=coord_x + 390, y=coord_y, width=60, height=25)

        def feat_pcon_u_e_onoff():
            if b_feat_pcon_u_e_onoff.cget ("bg") == rot:
                b_feat_pcon_u_e_onoff.configure (bg=gruen)
            elif b_feat_pcon_u_e_onoff.cget ("bg") == gruen:
                b_feat_pcon_u_e_onoff.configure (bg=rot)
        b_feat_pcon_u_e_onoff = tk.Button(f, font=('Courier New', 16, 'bold'), bg=rot, command=feat_pcon_u_e_onoff)
        b_feat_pcon_u_e_onoff.place (x=coord_x + 450, y=coord_y, width=20, height=25)

        def feat_pcon_u_e_buy():
            if b_feat_pcon_u_e_buy.cget ("bg") == gruen:
                b_feat_pcon_u_e_buy.configure (bg=rot)
            elif b_feat_pcon_u_e_buy.cget ("bg") == rot:
                b_feat_pcon_u_e_buy.configure (bg=gruen)
        b_feat_pcon_u_e_buy = tk.Button(f, text="BUY", font=('TkDefaultFont', 11, 'bold'), bg=gruen, command=feat_pcon_u_e_buy)
        b_feat_pcon_u_e_buy.place (x=coord_x + 480, y=coord_y, width=55, height=20)

        def feat_pcon_u_e_sell():
            if b_feat_pcon_u_e_sell.cget ("bg") == gruen:
                b_feat_pcon_u_e_sell.configure (bg=rot)
            elif b_feat_pcon_u_e_sell.cget ("bg") == rot:
                b_feat_pcon_u_e_sell.configure (bg=gruen)
        b_feat_pcon_u_e_sell = tk.Button(f, text="SELL", font=('TkDefaultFont', 11, 'bold'), bg=gruen, command=feat_pcon_u_e_sell)
        b_feat_pcon_u_e_sell.place (x=coord_x + 545, y=coord_y, width=55, height=20)


        # OVER
        coord_y += 30

        l_feat_pcon_over = tk.Label(f, text="OVER", font=('TkDefaultFont', 12, 'bold'), anchor="w", bg="#EEE8AA")
        l_feat_pcon_over.place (x=coord_x + 30, y=coord_y, width=60, height=25)

        e_feat_pcon_o_price = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_feat_pcon_o_price.place (x=coord_x + 100, y=coord_y, width=150, height=25)
        e_feat_pcon_o_price.insert (0, "9999999")

        def feat_pcon_o_buy():
            if b_feat_pcon_o_buy.cget ("bg") == gruen:
                b_feat_pcon_o_buy.configure (bg=rot)
            elif b_feat_pcon_o_buy.cget ("bg") == rot:
                b_feat_pcon_o_buy.configure (bg=gruen)
        b_feat_pcon_o_buy = tk.Button(f, text="BUY", font=('TkDefaultFont', 11, 'bold'), bg=gruen, command=feat_pcon_o_buy)
        b_feat_pcon_o_buy.place (x=coord_x + 260, y=coord_y, width=55, height=20)

        def feat_pcon_o_sell():
            if b_feat_pcon_o_sell.cget ("bg") == gruen:
                b_feat_pcon_o_sell.configure (bg=rot)
            elif b_feat_pcon_o_sell.cget ("bg") == rot:
                b_feat_pcon_o_sell.configure (bg=gruen)
        b_feat_pcon_o_sell = tk.Button(f, text="SELL", font=('TkDefaultFont', 11, 'bold'), bg=gruen, command=feat_pcon_o_sell)
        b_feat_pcon_o_sell.place (x=coord_x + 325, y=coord_y, width=55, height=20)

        l_feat_pcon_else_over = tk.Label(f, text="ELSE", font=('TkDefaultFont', 12, 'bold'), bg="#EEE8AA")
        l_feat_pcon_else_over.place (x=coord_x + 390, y=coord_y, width=60, height=25)


        def feat_pcon_o_e_onoff():
            if b_feat_pcon_o_e_onoff.cget ("bg") == rot:
                b_feat_pcon_o_e_onoff.configure (bg=gruen)
            elif b_feat_pcon_o_e_onoff.cget ("bg") == gruen:
                b_feat_pcon_o_e_onoff.configure (bg=rot)
        b_feat_pcon_o_e_onoff = tk.Button(f, font=('Courier New', 16, 'bold'), bg=rot, command=feat_pcon_o_e_onoff)
        b_feat_pcon_o_e_onoff.place (x=coord_x + 450, y=coord_y, width=20, height=25)

        def feat_pcon_o_e_buy():
            if b_feat_pcon_o_e_buy.cget ("bg") == gruen:
                b_feat_pcon_o_e_buy.configure (bg=rot)
            elif b_feat_pcon_o_e_buy.cget ("bg") == rot:
                b_feat_pcon_o_e_buy.configure (bg=gruen)
        b_feat_pcon_o_e_buy = tk.Button(f, text="BUY", font=('TkDefaultFont', 11, 'bold'), bg=gruen, command=feat_pcon_o_e_buy)
        b_feat_pcon_o_e_buy.place (x=coord_x + 480, y=coord_y, width=55, height=20)

        def feat_pcon_o_e_sell():
            if b_feat_pcon_o_e_sell.cget ("bg") == gruen:
                b_feat_pcon_o_e_sell.configure (bg=rot)
            elif b_feat_pcon_o_e_sell.cget ("bg") == rot:
                b_feat_pcon_o_e_sell.configure (bg=gruen)
        b_feat_pcon_o_e_sell = tk.Button(f, text="SELL", font=('TkDefaultFont', 11, 'bold'), bg=gruen, command=feat_pcon_o_e_sell)
        b_feat_pcon_o_e_sell.place (x=coord_x + 545, y=coord_y, width=55, height=20)

        # CAL
        coord_y += 35

        def feat_pcon_main():

            # ON/OFF prüfen
            if b_feat_pcon_onoff.cget ("bg") == rot:
                return

            # Price under
            if float(l_price.cget("text")) < float(e_feat_pcon_u_price.get()):

                # Else switch
                b_feat_pcon_u_e_onoff.configure (bg=gruen)
                b_feat_pcon_o_e_onoff.configure (bg=rot)

                # Buy side
                if b_feat_pcon_u_buy.cget("bg") == gruen:
                    b_feat_pcon_cal_buy.configure(bg=gruen)
                else:
                    b_feat_pcon_cal_buy.configure(bg=rot)
                # Sell side
                if b_feat_pcon_u_sell.cget("bg") == gruen:
                    b_feat_pcon_cal_sell.configure(bg=gruen)
                else:
                    b_feat_pcon_cal_sell.configure(bg=rot)

            # Price over
            elif float(l_price.cget("text")) > float(e_feat_pcon_o_price.get()):

                # Else switch
                b_feat_pcon_o_e_onoff.configure (bg=gruen)
                b_feat_pcon_u_e_onoff.configure (bg=rot)

                # Buy side
                if b_feat_pcon_o_buy.cget("bg") == gruen:
                    b_feat_pcon_cal_buy.configure(bg=gruen)
                else:
                    b_feat_pcon_cal_buy.configure(bg=rot)
                # Sell side
                if b_feat_pcon_o_sell.cget("bg") == gruen:
                    b_feat_pcon_cal_sell.configure(bg=gruen)
                else:
                    b_feat_pcon_cal_sell.configure(bg=rot)

            # Price else under
            elif b_feat_pcon_u_e_onoff.cget("bg") == gruen:

                # Buy side
                if b_feat_pcon_u_e_buy.cget("bg") == gruen:
                    b_feat_pcon_cal_buy.configure(bg=gruen)
                else:
                    b_feat_pcon_cal_buy.configure(bg=rot)
                # Sell side
                if b_feat_pcon_u_e_sell.cget("bg") == gruen:
                    b_feat_pcon_cal_sell.configure(bg=gruen)
                else:
                    b_feat_pcon_cal_sell.configure(bg=rot)

            # Price else over
            elif b_feat_pcon_o_e_onoff.cget("bg") == gruen:

                # Buy side
                if b_feat_pcon_o_e_buy.cget("bg") == gruen:
                    b_feat_pcon_cal_buy.configure(bg=gruen)
                else:
                    b_feat_pcon_cal_buy.configure(bg=rot)
                # Sell side
                if b_feat_pcon_o_e_sell.cget("bg") == gruen:
                    b_feat_pcon_cal_sell.configure(bg=gruen)
                else:
                    b_feat_pcon_cal_sell.configure(bg=rot)

        b_feat_pcon_cal = tk.Button(f, text="Cal", font=('Courier New', 16, 'bold'), command=feat_pcon_main)
        b_feat_pcon_cal.place (x=coord_x + 30, y=coord_y, width=50, height=25)

        def feat_pcon_cal_buy():
            if b_feat_pcon_cal_buy.cget ("bg") == gruen:
                b_feat_pcon_cal_buy.configure (bg=rot)
            elif b_feat_pcon_cal_buy.cget ("bg") == rot:
                b_feat_pcon_cal_buy.configure (bg=gruen)
        b_feat_pcon_cal_buy = tk.Button(f, text="BUY", font=('TkDefaultFont', 12, 'bold'), bg=gruen, command=feat_pcon_cal_buy)
        b_feat_pcon_cal_buy.place (x=coord_x + 100, y=coord_y, width=55, height=25)

        def feat_pcon_cal_sell():
            if b_feat_pcon_cal_sell.cget ("bg") == gruen:
                b_feat_pcon_cal_sell.configure (bg=rot)
            elif b_feat_pcon_cal_sell.cget ("bg") == rot:
                b_feat_pcon_cal_sell.configure (bg=gruen)
        b_feat_pcon_cal_sell = tk.Button(f, text="SELL", font=('TkDefaultFont', 12, 'bold'), bg=gruen, command=feat_pcon_cal_sell)
        b_feat_pcon_cal_sell.place (x=coord_x + 165, y=coord_y, width=55, height=25)

# COMMAND FELD (braunes Feld)
if 1==1:

    # Hintergrund
    area_command = tk.Label (f,relief="ridge", bg="#e7d7cc")
    area_command.place (x=15, y=340, width=665, height=260)

    # Stats LOG Buttons
    if 1==1:
        b_stats_load = tk.Button(f, text="L",command=stats_load)
        b_stats_load.place(x=460, y=575, width=20, height=20)

        b_stats_clear = tk.Button(f, text="C",command=stats_clear)
        b_stats_clear.place(x=485, y=575, width=20, height=20)


    # SEC INTERVALL
    if 1==1:
        coord_x = 590
        coord_y = 350
        
        l_bot_zeitd = tk.Label(f, text="000.000", font=('Courier New', 13, 'bold'),relief="ridge", anchor="c")
        l_bot_zeitd.place (x=coord_x - 130, y=coord_y, width=100, height=20)
        
        def sec_intervall_minus():
            wert = float(e_sec_intervall.get())
            e_sec_intervall.delete (0, "end")
            e_sec_intervall.insert (0, wert - 0.5)
        b_sec_intervall_minus = tk.Button (f, text="-", font=('Courier New', 18, 'bold'), command=sec_intervall_minus)
        b_sec_intervall_minus.place (x=coord_x - 25, y=coord_y, width=20, height=20)
        
        e_sec_intervall = tk.Entry (f,font=('Courier New', 14, 'bold'))
        e_sec_intervall.place (x=coord_x, y=coord_y, width=50, height=20)
        e_sec_intervall.insert (0, "3")

        def sec_intervall_plus():
            wert = float(e_sec_intervall.get())
            e_sec_intervall.delete (0, "end")
            e_sec_intervall.insert (0, wert + 0.5)
        b_sec_intervall_plus = tk.Button (f, text="+", font=('Courier New', 18, 'bold'), command=sec_intervall_plus)
        b_sec_intervall_plus.place (x=coord_x + 55, y=coord_y, width=20, height=20)
    
    # FILL
    if 1==1:
        coord_x = 460
        coord_y = 380
        
        # SIDE1 FILL
        e_fill = tk.Entry (f,font=('Courier New', 14, 'bold'))
        e_fill.place (x=coord_x, y=coord_y, width=100, height=20)

        def side1_fill_onoff():
            if b_fill_onoff.cget("bg") == rot:
                b_fill_onoff.configure (bg=gruen)
            else:
                b_fill_onoff.configure (bg=rot)
        b_fill_onoff = tk.Button (f, bg=gruen, command=side1_fill_onoff)
        b_fill_onoff.place (x=coord_x + 105, y=coord_y, width=15, height=20)


        def fill():
            if str(e_fill.get()) == "":
                return

            l_price.configure (text=float(e_fill.get()))
        b_fill = tk.Button (f, text="F", font=('TkDefaultFont', 11, 'bold'), command=fill)
        b_fill.place (x=coord_x + 125, y=coord_y, width=15, height=20)

        e_fill_loop = tk.Entry (f,font=('Courier New', 14, 'bold'))
        e_fill_loop.place (x=coord_x + 145, y=coord_y, width=30, height=20)
        e_fill_loop.insert (0, 1)


        class fill_buy_thread(Thread):
            def run(self):
                if b_fill_onoff.cget("bg") == gruen or float(e_main_price_buy.get()) == 0:
                    return
                
                if float(l_price.cget("text")) < float(e_main_price_buy.get()):
                    return


                for i in range(0, int(e_fill_loop.get())):

                    if b_funds_a2_onoff.cget("bg") == rot:
                        break

                    try:
                        while float(l_price.cget("text")) < float(e_main_price_buy.get()):
                            time.sleep (0.01)
                    except:
                        while str(e_main_price_buy.get()) == "":
                            time.sleep (0.01)


                    if b_main_bp_k.cget("text") == "%.0f":
                        wert = float(e_main_price_buy.get()) - 1
                    elif b_main_bp_k.cget("text") == "%.1f":
                        wert = float(e_main_price_buy.get()) - 0.1
                    elif b_main_bp_k.cget("text") == "%.2f":
                        wert = float(e_main_price_buy.get()) - 0.01
                    elif b_main_bp_k.cget("text") == "%.3f":
                        wert = float(e_main_price_buy.get()) - 0.001
                    elif b_main_bp_k.cget("text") == "%.4f":
                        wert = float(e_main_price_buy.get()) - 0.0001
                    elif b_main_bp_k.cget("text") == "%.5f":
                        wert = float(e_main_price_buy.get()) - 0.00001
                    elif b_main_bp_k.cget("text") == "%.6f":
                        wert = float(e_main_price_buy.get()) - 0.000001
                    elif b_main_bp_k.cget("text") == "%.7f":
                        wert = float(e_main_price_buy.get()) - 0.0000001
                    elif b_main_bp_k.cget("text") == "%.8f":
                        wert = float(e_main_price_buy.get()) - 0.00000001

                    l_price.configure (text= b_main_bp_k.cget("text") % wert)


        def fill_buy():
            fill_buy_thread().start()
        b_fill_buy = tk.Button (f, text="B", font=('TkDefaultFont', 7, 'bold'), command=fill_buy)
        b_fill_buy.place (x=coord_x + 180, y=coord_y, width=10, height=20)

        class fill_sell_thread(Thread):
            def run(self):
                if b_fill_onoff.cget("bg") == gruen or float(e_main_price_sell.get()) == 0:
                    return

                if float(l_price.cget("text")) > float(e_main_price_sell.get()):
                    return

                for i in range(0, int(e_fill_loop.get())):

                    if b_funds_a1_onoff.cget("bg") == rot:
                        break

                    try:
                        while float(l_price.cget("text")) > float(e_main_price_sell.get()):
                            time.sleep (0.01)
                    except:
                        while str(e_main_price_sell.get()) == "":
                            time.sleep (0.01)


                    if b_main_bp_k.cget("text") == "%.0f":
                        wert = float(e_main_price_sell.get()) + 1
                    elif b_main_bp_k.cget("text") == "%.1f":
                        wert = float(e_main_price_sell.get()) + 0.1
                    elif b_main_bp_k.cget("text") == "%.2f":
                        wert = float(e_main_price_sell.get()) + 0.01
                    elif b_main_bp_k.cget("text") == "%.3f":
                        wert = float(e_main_price_sell.get()) + 0.001
                    elif b_main_bp_k.cget("text") == "%.4f":
                        wert = float(e_main_price_sell.get()) + 0.0001
                    elif b_main_bp_k.cget("text") == "%.5f":
                        wert = float(e_main_price_sell.get()) + 0.00001
                    elif b_main_bp_k.cget("text") == "%.6f":
                        wert = float(e_main_price_sell.get()) + 0.000001
                    elif b_main_bp_k.cget("text") == "%.7f":
                        wert = float(e_main_price_sell.get()) + 0.0000001
                    elif b_main_bp_k.cget("text") == "%.8f":
                        wert = float(e_main_price_sell.get()) + 0.00000001

                    l_price.configure (text= b_main_bp_k.cget("text") % wert)


        def fill_sell():
            fill_sell_thread().start()
        b_fill_sell = tk.Button (f, text="S", font=('TkDefaultFont', 7, 'bold'), command=fill_sell)
        b_fill_sell.place (x=coord_x + 195, y=coord_y, width=10, height=20)

    # Pair
    if 1==1:
        coord_x = 460
        coord_y = 410
        
        
        e_pair = tk.Entry(f, font=('Courier New', 18, 'bold'))
        e_pair.place (x=coord_x, y=coord_y, width=180, height=25)
        e_pair.insert (0, "BTCUSDT")

        l_price = tk.Label (f, text="0.00000000", font=('Courier New', 25, 'bold'), bg="#B0E2FF", anchor="w")
        l_price.place (x=coord_x, y=coord_y + 35, width=205, height=35)

        class get_price_thread(Thread):
            def run(self):

                l_price.configure (text="------")
                
                api_price = "https://api.binance.com/api/v1/ticker/price?symbol=" + e_pair.get().upper()
                try:
                    r = requests.get(url=api_price, timeout=4)
                    l_price.configure (text=float(r.json() ["price"]))
                except:
                    try:
                        t_log_all.insert ("1.0", r.text + "\n\n")
                        t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  KURS HOLEN FAIL\n")
                    except:
                        t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  KURS HOLEN KRIT FAIL\n")
        def get_price():
            get_price_thread().start()
        b_get_price = tk.Button (f, text="T", font=('Courier New', 18, 'bold'), command=get_price)
        b_get_price.place (x=coord_x + 185, y=coord_y, width=20, height=25)

    # BUTTONS  :  START / STOP / SIM / DOCU
    if 1==1:
        coord_x = 460
        coord_y = 490

        def bot_starten():
            bot_starten_thread().start()
        b_bot_start = tk.Button (f, text="START", font=("TkDefaultFont", 9, 'bold'), bg="#cb8d73", command=bot_starten)
        b_bot_start.place (x=coord_x, y=coord_y, width=45, height=30)

        def bot_stopen():
            global bot_start
            bot_start = 0
        b_bot_stop = tk.Button (f, text="X", font=("TkDefaultFont", 9, 'bold'), bg="#cb8d73", command=bot_stopen)
        b_bot_stop.place (x=coord_x + 55, y=coord_y, width=45, height=30)

        def bot_sim_onoff():
            if b_bot_sim_onoff.cget ("bg") == rot and b_bot_start.cget ("bg") == "#cb8d73":
                b_bot_sim_onoff.configure (bg=gruen)
                b_nbot_template.configure (text="S_" + str(b_nbot_template.cget ("text")))
                area_bot.configure (bg="#E0E0F8")
                
            elif b_bot_sim_onoff.cget ("bg") == gruen and b_bot_start.cget ("bg") == "#cb8d73":
                b_bot_sim_onoff.configure (bg=rot)
                if str(b_nbot_template.cget ("text")).find ("S_") >= 0:
                    b_nbot_template.configure (text=str(b_nbot_template.cget ("text"))[2:] )
                area_bot.configure (bg="#EEE8AA")
       
        b_bot_sim_onoff = tk.Button (f, text="SIM", font=("TkDefaultFont", 12, 'bold'), bg=rot, command=bot_sim_onoff)
        b_bot_sim_onoff.place (x=coord_x + 120, y=coord_y, width=40, height=25)

        def bot_docu_onoff():
            if b_bot_docu_onoff.cget("bg") == gruen:
                b_bot_docu_onoff.configure (bg=rot)
            else:
                b_bot_docu_onoff.configure (bg=gruen)
        b_bot_docu_onoff = tk.Button (f, text="Docu", font=("TkDefaultFont", 10, 'bold'), bg=gruen, command=bot_docu_onoff)
        b_bot_docu_onoff.place (x=coord_x + 165, y=coord_y, width=40, height=25)

    # Funds
    if 1==1:
        class allfunds_thread(Thread):
            def run(self):
                
                summe = 0

                # Time Sync
                if b_timek.cget ("text") == 0:
                    timek()
                t_str = "%.0f" % (time.time() * 1000 + b_timek.cget ("text"))

                # Funds Anfrage senden
                base_url = "https://api.binance.com/api/v3/account?"
                query = "timestamp=" + t_str + "&recvWindow=20000"

                signature = hmac.new(s_key.encode("utf-8"), query.encode("utf-8"), hashlib.sha256).hexdigest()
                sign_end = "&signature=" + signature

                url_rdy = base_url + query + sign_end
                header = {'X-MBX-APIKEY' : a_key}

                try:
                    r = requests.get (url_rdy, headers=header)

                    balance_list = r.json() ["balances"]

                    t_log_all.insert ("1.0", "\n")
                    
                    for i in range (0, len(balance_list)):

                        # Check All Funds
                        if 1 == 1:

                            if float(balance_list[i] ["free"]) > 0.000000009 or float(balance_list[i] ["locked"]) > 0.000000009:

                                free = "%.8f" % float(balance_list[i]["free"])
                                locked = "%.8f" % float(balance_list[i]["locked"])
                                    
                                # Ordnen 1
                                if 1==1:
                                    if len(balance_list[i]["asset"]) == 8:
                                        leer1 = ""
                                    elif len(balance_list[i]["asset"]) == 7:
                                        leer1 = " "
                                    elif len(balance_list[i]["asset"]) == 6:
                                        leer1 = "  "
                                    elif len(balance_list[i]["asset"]) == 5:
                                        leer1 = "   "
                                    elif len(balance_list[i]["asset"]) == 4:
                                        leer1 = "    "
                                    elif len(balance_list[i]["asset"]) == 3:
                                        leer1 = "     "
                                    elif len(balance_list[i]["asset"]) == 2:
                                        leer1 = "      "
                                    else:
                                        leer1 = " "

                                # Ordnen nach Punkten 1
                                if 1==1:
                                    if free.find (".") == 8:
                                        leer1 = leer1 + ""
                                    elif free.find (".") == 7:
                                        leer1 = leer1 + " "
                                    elif free.find (".") == 6:
                                        leer1 = leer1 + "  "
                                    elif free.find (".") == 5:
                                        leer1 = leer1 + "   "
                                    elif free.find (".") == 4:
                                        leer1 = leer1 + "    "
                                    elif free.find (".") == 3:
                                        leer1 = leer1 + "     "
                                    elif free.find (".") == 2:
                                        leer1 = leer1 + "      "
                                    elif free.find (".") == 1:
                                        leer1 = leer1 + "       "

                                # Price holen
                                if balance_list[i] ["asset"] == "LUNA":
                                    fund_price = "https://api.binance.com/api/v1/ticker/price?symbol=" + balance_list[i] ["asset"] + "BUSD"
                                    try:
                                        r = requests.get(url=fund_price, timeout=4)
                                        testen_price = float(r.json() ["price"])
                                        saldo = "%.2f" % ((testen_price * float(balance_list[i]["free"])) + (testen_price * float(balance_list[i]["locked"])))
                                    except:
                                        saldo = "0.00"
                                
                                elif not balance_list[i] ["asset"] == "USDT":
                                    fund_price = "https://api.binance.com/api/v1/ticker/price?symbol=" + balance_list[i] ["asset"] + "USDT"
                                    try:
                                        r = requests.get(url=fund_price, timeout=4)
                                        testen_price = float(r.json() ["price"])
                                        saldo = "%.2f" % ((testen_price * float(balance_list[i]["free"])) + (testen_price * float(balance_list[i]["locked"])))
                                    except:
                                        saldo = "0.00"
                                if balance_list[i] ["asset"] == "USDT":
                                    saldo = "%.2f" % (float(balance_list[i]["free"]) + float(balance_list[i]["locked"]))

                                if not balance_list[i] ["asset"] == "BNB":
                                    summe += float(saldo)

                                t_log_all.insert ("1.0", balance_list[i]["asset"] + leer1 + free + "  " + locked + "  " + saldo + "\n")


                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + " FUNDS  " + "%.0f" % summe + "\n")

                except Exception as e:
                    t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "  <GET FUNDS FAIL>\nEXCEPTION: " + str(e) + "\nRESPONSE: " + r.text + "\n\n")
                    
                    if r.text.find ("Timestamp") > 0:
                        timek()

        def allfunds():
            allfunds_thread().start()
        b_funds = tk.Button (f, text="FUNDS", font=('Courier New', 14, 'bold'), command=allfunds)
        b_funds.place (x=605, y=575, width=70, height=17)

    # FEAT MA FOLLOW
    if 1==1:
        coord_x = 20
        coord_y = 350

        # Main
        if 1==1:

            def feat_maf_main():

                maf = feat_maf_get_thread()
                maf.start()
                maf.join()

                feat_maf_lines_cal()

                if float(l_price.cget("text")) == 0:
                    return

                # BUY/SELL Stellung auslesen
                if float(l_price.cget("text")) > float(e_feat_maf_line7_erg.get()) and float(e_feat_maf_line7_erg.get()) > 0:
                    switch_buy = int(e_feat_maf_line7_buy.get())
                    switch_sell = int(e_feat_maf_line7_sell.get())
                    e_feat_maf_line1_erg.configure (bg="white")
                    e_feat_maf_line2_erg.configure (bg="white")
                    e_feat_maf_line3_erg.configure (bg="white")
                    e_feat_maf_line4_erg.configure (bg="white")
                    e_feat_maf_line5_erg.configure (bg="white")
                    e_feat_maf_line6_erg.configure (bg="white")
                    e_feat_maf_line7_erg.configure (bg=blau)
                elif float(l_price.cget("text")) > float(e_feat_maf_line6_erg.get()) and float(e_feat_maf_line6_erg.get()) > 0:
                    switch_buy = int(e_feat_maf_line6_buy.get())
                    switch_sell = int(e_feat_maf_line6_sell.get())
                    e_feat_maf_line1_erg.configure (bg="white")
                    e_feat_maf_line2_erg.configure (bg="white")
                    e_feat_maf_line3_erg.configure (bg="white")
                    e_feat_maf_line4_erg.configure (bg="white")
                    e_feat_maf_line5_erg.configure (bg="white")
                    e_feat_maf_line6_erg.configure (bg=blau)
                    e_feat_maf_line7_erg.configure (bg="white")
                elif float(l_price.cget("text")) > float(e_feat_maf_line5_erg.get()) and float(e_feat_maf_line5_erg.get()) > 0:
                    switch_buy = int(e_feat_maf_line5_buy.get())
                    switch_sell = int(e_feat_maf_line5_sell.get())
                    e_feat_maf_line1_erg.configure (bg="white")
                    e_feat_maf_line2_erg.configure (bg="white")
                    e_feat_maf_line3_erg.configure (bg="white")
                    e_feat_maf_line4_erg.configure (bg="white")
                    e_feat_maf_line5_erg.configure (bg=blau)
                    e_feat_maf_line6_erg.configure (bg="white")
                    e_feat_maf_line7_erg.configure (bg="white")
                elif float(l_price.cget("text")) > float(e_feat_maf_line4_erg.get()) and float(e_feat_maf_line4_erg.get()) > 0:
                    switch_buy = int(e_feat_maf_line4_buy.get())
                    switch_sell = int(e_feat_maf_line4_sell.get())
                    e_feat_maf_line1_erg.configure (bg="white")
                    e_feat_maf_line2_erg.configure (bg="white")
                    e_feat_maf_line3_erg.configure (bg="white")
                    e_feat_maf_line4_erg.configure (bg=blau)
                    e_feat_maf_line5_erg.configure (bg="white")
                    e_feat_maf_line6_erg.configure (bg="white")
                    e_feat_maf_line7_erg.configure (bg="white")
                elif float(l_price.cget("text")) > float(e_feat_maf_line3_erg.get()) and float(e_feat_maf_line3_erg.get()) > 0:
                    switch_buy = int(e_feat_maf_line3_buy.get())
                    switch_sell = int(e_feat_maf_line3_sell.get())
                    e_feat_maf_line1_erg.configure (bg="white")
                    e_feat_maf_line2_erg.configure (bg="white")
                    e_feat_maf_line3_erg.configure (bg=blau)
                    e_feat_maf_line4_erg.configure (bg="white")
                    e_feat_maf_line5_erg.configure (bg="white")
                    e_feat_maf_line6_erg.configure (bg="white")
                    e_feat_maf_line7_erg.configure (bg="white")
                elif float(l_price.cget("text")) > float(e_feat_maf_line2_erg.get()) and float(e_feat_maf_line2_erg.get()) > 0:
                    switch_buy = int(e_feat_maf_line2_buy.get())
                    switch_sell = int(e_feat_maf_line2_sell.get())
                    e_feat_maf_line1_erg.configure (bg="white")
                    e_feat_maf_line2_erg.configure (bg=blau)
                    e_feat_maf_line3_erg.configure (bg="white")
                    e_feat_maf_line4_erg.configure (bg="white")
                    e_feat_maf_line5_erg.configure (bg="white")
                    e_feat_maf_line6_erg.configure (bg="white")
                    e_feat_maf_line7_erg.configure (bg="white")
                elif float(l_price.cget("text")) > float(e_feat_maf_line1_erg.get()) and float(e_feat_maf_line1_erg.get()) > 0:
                    switch_buy = int(e_feat_maf_line1_buy.get())
                    switch_sell = int(e_feat_maf_line1_sell.get())
                    e_feat_maf_line1_erg.configure (bg=blau)
                    e_feat_maf_line2_erg.configure (bg="white")
                    e_feat_maf_line3_erg.configure (bg="white")
                    e_feat_maf_line4_erg.configure (bg="white")
                    e_feat_maf_line5_erg.configure (bg="white")
                    e_feat_maf_line6_erg.configure (bg="white")
                    e_feat_maf_line7_erg.configure (bg="white")
                else:
                    switch_buy = 0
                    switch_sell = 0
                    e_feat_maf_line1_erg.configure (bg="white")
                    e_feat_maf_line2_erg.configure (bg="white")
                    e_feat_maf_line3_erg.configure (bg="white")
                    e_feat_maf_line4_erg.configure (bg="white")
                    e_feat_maf_line5_erg.configure (bg="white")
                    e_feat_maf_line6_erg.configure (bg="white")
                    e_feat_maf_line7_erg.configure (bg="white")
        
                # BUY
                if switch_buy == 1:
                    b_main_price_buy_onoff.configure (bg=gruen)
                    b_main_price_buy2_onoff.configure (bg=rot)
                    b_main_price_buy3_onoff.configure (bg=rot)
                    b_main_price_buy4_onoff.configure (bg=rot)
                    b_main_price_buy5_onoff.configure (bg=rot)
                elif switch_buy == 2:
                    b_main_price_buy_onoff.configure (bg=rot)
                    b_main_price_buy2_onoff.configure (bg=gruen)
                    b_main_price_buy3_onoff.configure (bg=rot)
                    b_main_price_buy4_onoff.configure (bg=rot)
                    b_main_price_buy5_onoff.configure (bg=rot)
                elif switch_buy == 3:
                    b_main_price_buy_onoff.configure (bg=rot)
                    b_main_price_buy2_onoff.configure (bg=rot)
                    b_main_price_buy3_onoff.configure (bg=gruen)
                    b_main_price_buy4_onoff.configure (bg=rot)
                    b_main_price_buy5_onoff.configure (bg=rot)
                elif switch_buy == 4:
                    b_main_price_buy_onoff.configure (bg=rot)
                    b_main_price_buy2_onoff.configure (bg=rot)
                    b_main_price_buy3_onoff.configure (bg=rot)
                    b_main_price_buy4_onoff.configure (bg=gruen)
                    b_main_price_buy5_onoff.configure (bg=rot)
                elif switch_buy == 5:
                    b_main_price_buy_onoff.configure (bg=rot)
                    b_main_price_buy2_onoff.configure (bg=rot)
                    b_main_price_buy3_onoff.configure (bg=rot)
                    b_main_price_buy4_onoff.configure (bg=rot)
                    b_main_price_buy5_onoff.configure (bg=gruen)

                # SELL
                if switch_sell == 1:
                    b_main_price_sell_onoff.configure (bg=gruen)
                    b_main_price_sell2_onoff.configure (bg=rot)
                    b_main_price_sell3_onoff.configure (bg=rot)
                    b_main_price_sell4_onoff.configure (bg=rot)
                    b_main_price_sell5_onoff.configure (bg=rot)
                elif switch_sell == 2:
                    b_main_price_sell_onoff.configure (bg=rot)
                    b_main_price_sell2_onoff.configure (bg=gruen)
                    b_main_price_sell3_onoff.configure (bg=rot)
                    b_main_price_sell4_onoff.configure (bg=rot)
                    b_main_price_sell5_onoff.configure (bg=rot)
                elif switch_sell == 3:
                    b_main_price_sell_onoff.configure (bg=rot)
                    b_main_price_sell2_onoff.configure (bg=rot)
                    b_main_price_sell3_onoff.configure (bg=gruen)
                    b_main_price_sell4_onoff.configure (bg=rot)
                    b_main_price_sell5_onoff.configure (bg=rot)
                elif switch_sell == 4:
                    b_main_price_sell_onoff.configure (bg=rot)
                    b_main_price_sell2_onoff.configure (bg=rot)
                    b_main_price_sell3_onoff.configure (bg=rot)
                    b_main_price_sell4_onoff.configure (bg=gruen)
                    b_main_price_sell5_onoff.configure (bg=rot)
                elif switch_sell == 5:
                    b_main_price_sell_onoff.configure (bg=rot)
                    b_main_price_sell2_onoff.configure (bg=rot)
                    b_main_price_sell3_onoff.configure (bg=rot)
                    b_main_price_sell4_onoff.configure (bg=rot)
                    b_main_price_sell5_onoff.configure (bg=gruen)



            def feat_maf_onoff():
                if b_feat_maf_onoff.cget ("bg") == rot:
                    b_feat_maf_onoff.configure (bg=gruen)
                elif b_feat_maf_onoff.cget ("bg") == gruen:
                    b_feat_maf_onoff.configure (bg=rot)
            b_feat_maf_onoff = tk.Button(f,bg=rot, command=feat_maf_onoff)
            b_feat_maf_onoff.place(x=coord_x, y=coord_y, width=20, height=20)
            
            class feat_maf_get_thread(Thread):
                def run(self):

                    try:
                        r = requests.get ("https://api.binance.com/api/v3/klines?symbol=" + str(e_pair.get()).upper() + "&limit=" + str(e_feat_maf_limit.get()) + "&interval=" + b_feat_maf_interval.cget ("text"), timeout=4)                    

                        # Kerzen_ma ergebnisse einfügen
                        summe_ma1 = 0
                        for i in range (len(r.json()) - 1, len(r.json()) - int(e_feat_maf_limit.get()) - 1, -1):
                            summe_ma1 += float(r.json()[i][4])
                        
                        e_feat_maf_kurs.delete (0, "end")
                        e_feat_maf_kurs.insert (0, b_feat_maf_k.cget("text") % (summe_ma1 / int(e_feat_maf_limit.get())))

                        # Prozente differenz zum Kurs
                        if not float(l_price.cget("text")) == 0:
                            l_feat_maf_get_diff.configure  (text="%.2f" % ((float(l_price.cget("text")) / (float(e_feat_maf_kurs.get()) / 100)) - 100))

                    except:
                        try:
                            t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "<FEAT-MAF GET FAIL>\n" + r.text[0:400] + "\n\n")
                        except:
                            t_log_all.insert ("1.0", time.strftime("%d.%m.%y %H:%M:%S") + "<FEAT-MAF GET KRIT FAIL>\n\n")

            def feat_maf_get():
                feat_maf_get_thread().start()
            
            b_feat_maf_get = tk.Button(f,text="G", font=('Courier New', 14, 'bold'), command=feat_maf_get)
            b_feat_maf_get.place(x=coord_x + 25, y=coord_y, width=20, height=20)

            def feat_maf_interval():
                if b_feat_maf_interval.cget ("text") == "1m":
                    b_feat_maf_interval.configure (text="3m")
                elif b_feat_maf_interval.cget ("text") == "3m":
                    b_feat_maf_interval.configure (text="5m")
                elif b_feat_maf_interval.cget ("text") == "5m":
                    b_feat_maf_interval.configure (text="15m")
                elif b_feat_maf_interval.cget ("text") == "15m":
                    b_feat_maf_interval.configure (text="30m")
                elif b_feat_maf_interval.cget ("text") == "30m":
                    b_feat_maf_interval.configure (text="1h")
                elif b_feat_maf_interval.cget ("text") == "1h":
                    b_feat_maf_interval.configure (text="2h")
                elif b_feat_maf_interval.cget ("text") == "2h":
                    b_feat_maf_interval.configure (text="4h")
                elif b_feat_maf_interval.cget ("text") == "4h":
                    b_feat_maf_interval.configure (text="6h")
                elif b_feat_maf_interval.cget ("text") == "6h":
                    b_feat_maf_interval.configure (text="8h")
                elif b_feat_maf_interval.cget ("text") == "8h":
                    b_feat_maf_interval.configure (text="12h")
                elif b_feat_maf_interval.cget ("text") == "12h":
                    b_feat_maf_interval.configure (text="1d")
                elif b_feat_maf_interval.cget ("text") == "1d":
                    b_feat_maf_interval.configure (text="3d")
                elif b_feat_maf_interval.cget ("text") == "3d":
                    b_feat_maf_interval.configure (text="1w")
                elif b_feat_maf_interval.cget ("text") == "1w":
                    b_feat_maf_interval.configure (text="1M")
                elif b_feat_maf_interval.cget ("text") == "1M":
                    b_feat_maf_interval.configure (text="1m")
            b_feat_maf_interval = tk.Button (f,text="1m", font=('Courier New', 14, 'bold'), command=feat_maf_interval)
            b_feat_maf_interval.place (x=coord_x + 50, y=coord_y, width=40, height=20)

            e_feat_maf_limit = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_limit.place (x=coord_x + 95, y=coord_y, width=40, height=20)
            e_feat_maf_limit.insert (0, 100)

            e_feat_maf_kurs = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken", bg="#ECCEF5")
            e_feat_maf_kurs.place (x=coord_x + 145, y=coord_y, width=125, height=20)
            e_feat_maf_kurs.insert (0, 0)

            def feat_maf_k():
                if b_feat_maf_k.cget ("text") == "%.0f":
                    b_feat_maf_k.configure (text="%.1f")
                elif b_feat_maf_k.cget ("text") == "%.1f":
                    b_feat_maf_k.configure (text="%.2f")
                elif b_feat_maf_k.cget ("text") == "%.2f":
                    b_feat_maf_k.configure (text="%.3f")
                elif b_feat_maf_k.cget ("text") == "%.3f":
                    b_feat_maf_k.configure (text="%.4f")
                elif b_feat_maf_k.cget ("text") == "%.4f":
                    b_feat_maf_k.configure (text="%.5f")
                elif b_feat_maf_k.cget ("text") == "%.5f":
                    b_feat_maf_k.configure (text="%.6f")
                elif b_feat_maf_k.cget ("text") == "%.6f":
                    b_feat_maf_k.configure (text="%.7f")
                elif b_feat_maf_k.cget ("text") == "%.7f":
                    b_feat_maf_k.configure (text="%.8f")
                elif b_feat_maf_k.cget ("text") == "%.8f":
                    b_feat_maf_k.configure (text="%.0f")
            b_feat_maf_k = tk.Button(f, text="%.2f", font=('Courier New', 14, 'bold'), command=feat_maf_k)
            b_feat_maf_k.place (x=coord_x + 275, y=coord_y, width=45, height=20)

            e_feat_maf_round = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_round.place (x=coord_x, y=coord_y + 25, width=50, height=20)
            e_feat_maf_round.insert (0, 10)

            def feat_maf_round_in():
                l_feat_maf_round_use.configure (text=int(e_feat_maf_round.get()))
            b_feat_maf_round_in = tk.Button(f, text="IN", font=('Courier New', 14, 'bold'), command=feat_maf_round_in)
            b_feat_maf_round_in.place (x=coord_x + 55, y=coord_y + 25, width=35, height=20)

            l_feat_maf_round_use = tk.Label (f,text=0, font=('Courier New', 14, 'bold'))
            l_feat_maf_round_use.place (x=coord_x + 95, y=coord_y + 25, width=50, height=20)

            l_feat_maf_get_diff = tk.Label (f,text= "00.00", font=('Courier New', 14, 'bold'))
            l_feat_maf_get_diff.place (x=coord_x + 160, y=coord_y + 25, width=110, height=20)

            # Calculator
            e_feat_maf_cal_pro = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_cal_pro.place (x=coord_x + 330, y=coord_y, width=50, height=20)
            e_feat_maf_cal_pro.insert (0, 10)

            def feat_maf_cal():
                if float(e_feat_maf_kurs.get()) == 0:
                    return
                e_feat_maf_cal_erg.delete  (0, "end")
                e_feat_maf_cal_erg.insert (0, b_feat_maf_k.cget("text") % (float(e_feat_maf_kurs.get()) / 100 * (100 + float(e_feat_maf_cal_pro.get()))))
            b_feat_maf_cal = tk.Button(f, text="Cal", font=('Courier New', 14, 'bold'), command=feat_maf_cal)
            b_feat_maf_cal.place (x=coord_x + 385, y=coord_y, width=45, height=20)

            e_feat_maf_cal_erg = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken")
            e_feat_maf_cal_erg.place (x=coord_x + 305, y=coord_y + 25, width=125, height=20)
            e_feat_maf_cal_erg.insert (0, 0)

        # Lines
        if 1==1:
            
            # Line 1
            coord_y += 65
            e_feat_maf_line1_pro = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line1_pro.place (x=coord_x, y=coord_y - 10, width=60, height=20)
            e_feat_maf_line1_pro.insert (0, 10)

            e_feat_maf_line1_erg = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken")
            e_feat_maf_line1_erg.place (x=coord_x + 70, y=coord_y, width=125, height=20)
            e_feat_maf_line1_erg.insert (0, 0)

            l_feat_maf_line1_buy = tk.Label (f,text= "B:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line1_buy.place (x=coord_x + 205, y=coord_y, width=25, height=20)

            e_feat_maf_line1_buy = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line1_buy.place (x=coord_x + 235, y=coord_y, width=30, height=20)
            e_feat_maf_line1_buy.insert (0, 1)

            l_feat_maf_line1_sell = tk.Label (f,text= "S:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line1_sell.place (x=coord_x + 275, y=coord_y, width=25, height=20)

            e_feat_maf_line1_sell = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line1_sell.place (x=coord_x + 305, y=coord_y, width=30, height=20)
            e_feat_maf_line1_sell.insert (0, 1)

            # Line 2
            coord_y += 25
            e_feat_maf_line2_pro = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line2_pro.place (x=coord_x, y=coord_y - 10, width=60, height=20)
            e_feat_maf_line2_pro.insert (0, 0)

            e_feat_maf_line2_erg = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken")
            e_feat_maf_line2_erg.place (x=coord_x + 70, y=coord_y, width=125, height=20)
            e_feat_maf_line2_erg.insert (0, 0)

            l_feat_maf_line2_buy = tk.Label (f,text= "B:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line2_buy.place (x=coord_x + 205, y=coord_y, width=25, height=20)

            e_feat_maf_line2_buy = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line2_buy.place (x=coord_x + 235, y=coord_y, width=30, height=20)
            e_feat_maf_line2_buy.insert (0, 1)

            l_feat_maf_line2_sell = tk.Label (f,text= "S:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line2_sell.place (x=coord_x + 275, y=coord_y, width=25, height=20)

            e_feat_maf_line2_sell = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line2_sell.place (x=coord_x + 305, y=coord_y, width=30, height=20)
            e_feat_maf_line2_sell.insert (0, 1)

            # Line 3
            coord_y += 25
            e_feat_maf_line3_pro = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line3_pro.place (x=coord_x, y=coord_y - 10, width=60, height=20)
            e_feat_maf_line3_pro.insert (0, 0)

            e_feat_maf_line3_erg = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken")
            e_feat_maf_line3_erg.place (x=coord_x + 70, y=coord_y, width=125, height=20)
            e_feat_maf_line3_erg.insert (0, 0)

            l_feat_maf_line3_buy = tk.Label (f,text= "B:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line3_buy.place (x=coord_x + 205, y=coord_y, width=25, height=20)

            e_feat_maf_line3_buy = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line3_buy.place (x=coord_x + 235, y=coord_y, width=30, height=20)
            e_feat_maf_line3_buy.insert (0, 1)

            l_feat_maf_line3_sell = tk.Label (f,text= "S:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line3_sell.place (x=coord_x + 275, y=coord_y, width=25, height=20)

            e_feat_maf_line3_sell = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line3_sell.place (x=coord_x + 305, y=coord_y, width=30, height=20)
            e_feat_maf_line3_sell.insert (0, 1)


            # Line 4
            coord_y += 25
            e_feat_maf_line4_pro = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line4_pro.place (x=coord_x, y=coord_y - 10, width=60, height=20)
            e_feat_maf_line4_pro.insert (0, 0)

            e_feat_maf_line4_erg = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken")
            e_feat_maf_line4_erg.place (x=coord_x + 70, y=coord_y, width=125, height=20)
            e_feat_maf_line4_erg.insert (0, 0)

            l_feat_maf_line4_buy = tk.Label (f,text= "B:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line4_buy.place (x=coord_x + 205, y=coord_y, width=25, height=20)

            e_feat_maf_line4_buy = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line4_buy.place (x=coord_x + 235, y=coord_y, width=30, height=20)
            e_feat_maf_line4_buy.insert (0, 1)

            l_feat_maf_line4_sell = tk.Label (f,text= "S:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line4_sell.place (x=coord_x + 275, y=coord_y, width=25, height=20)

            e_feat_maf_line4_sell = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line4_sell.place (x=coord_x + 305, y=coord_y, width=30, height=20)
            e_feat_maf_line4_sell.insert (0, 1)


            # Line 5
            coord_y += 25
            e_feat_maf_line5_pro = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line5_pro.place (x=coord_x, y=coord_y - 10, width=60, height=20)
            e_feat_maf_line5_pro.insert (0, 0)

            e_feat_maf_line5_erg = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken")
            e_feat_maf_line5_erg.place (x=coord_x + 70, y=coord_y, width=125, height=20)
            e_feat_maf_line5_erg.insert (0, 0)

            l_feat_maf_line5_buy = tk.Label (f,text= "B:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line5_buy.place (x=coord_x + 205, y=coord_y, width=25, height=20)

            e_feat_maf_line5_buy = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line5_buy.place (x=coord_x + 235, y=coord_y, width=30, height=20)
            e_feat_maf_line5_buy.insert (0, 1)

            l_feat_maf_line5_sell = tk.Label (f,text= "S:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line5_sell.place (x=coord_x + 275, y=coord_y, width=25, height=20)

            e_feat_maf_line5_sell = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line5_sell.place (x=coord_x + 305, y=coord_y, width=30, height=20)
            e_feat_maf_line5_sell.insert (0, 1)


            # Line 6
            coord_y += 25
            e_feat_maf_line6_pro = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line6_pro.place (x=coord_x, y=coord_y - 10, width=60, height=20)
            e_feat_maf_line6_pro.insert (0, 0)

            e_feat_maf_line6_erg = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken")
            e_feat_maf_line6_erg.place (x=coord_x + 70, y=coord_y, width=125, height=20)
            e_feat_maf_line6_erg.insert (0, 0)

            l_feat_maf_line6_buy = tk.Label (f,text= "B:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line6_buy.place (x=coord_x + 205, y=coord_y, width=25, height=20)

            e_feat_maf_line6_buy = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line6_buy.place (x=coord_x + 235, y=coord_y, width=30, height=20)
            e_feat_maf_line6_buy.insert (0, 1)

            l_feat_maf_line6_sell = tk.Label (f,text= "S:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line6_sell.place (x=coord_x + 275, y=coord_y, width=25, height=20)

            e_feat_maf_line6_sell = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line6_sell.place (x=coord_x + 305, y=coord_y, width=30, height=20)
            e_feat_maf_line6_sell.insert (0, 1)

            # Line 7
            coord_y += 25
            e_feat_maf_line7_pro = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line7_pro.place (x=coord_x, y=coord_y - 10, width=60, height=20)
            e_feat_maf_line7_pro.insert (0, 0)

            e_feat_maf_line7_erg = tk.Entry (f, font=('Courier New', 15, 'bold'), relief="sunken")
            e_feat_maf_line7_erg.place (x=coord_x + 70, y=coord_y, width=125, height=20)
            e_feat_maf_line7_erg.insert (0, 0)

            l_feat_maf_line7_buy = tk.Label (f,text= "B:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line7_buy.place (x=coord_x + 205, y=coord_y, width=25, height=20)

            e_feat_maf_line7_buy = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line7_buy.place (x=coord_x + 235, y=coord_y, width=30, height=20)
            e_feat_maf_line7_buy.insert (0, 1)

            l_feat_maf_line7_sell = tk.Label (f,text= "S:", font=('Courier New', 16, 'bold'), bg="#e7d7cc")
            l_feat_maf_line7_sell.place (x=coord_x + 275, y=coord_y, width=25, height=20)

            e_feat_maf_line7_sell = tk.Entry (f,font=('Courier New', 14, 'bold'))
            e_feat_maf_line7_sell.place (x=coord_x + 305, y=coord_y, width=30, height=20)
            e_feat_maf_line7_sell.insert (0, 1)

            # Calculation
            coord_y -= 125
            def feat_maf_lines_cal():
                if not float(e_feat_maf_line1_pro.get()) == 0:
                    e_feat_maf_line1_erg.delete  (0, "end")
                    e_feat_maf_line1_erg.insert (0, b_feat_maf_k.cget("text") % (float(e_feat_maf_kurs.get()) / 100 * (100 + float(e_feat_maf_line1_pro.get()))))
                if not float(e_feat_maf_line2_pro.get()) == 0:
                    e_feat_maf_line2_erg.delete  (0, "end")
                    e_feat_maf_line2_erg.insert (0, b_feat_maf_k.cget("text") % (float(e_feat_maf_kurs.get()) / 100 * (100 + float(e_feat_maf_line2_pro.get()))))
                if not float(e_feat_maf_line3_pro.get()) == 0:
                    e_feat_maf_line3_erg.delete  (0, "end")
                    e_feat_maf_line3_erg.insert (0, b_feat_maf_k.cget("text") % (float(e_feat_maf_kurs.get()) / 100 * (100 + float(e_feat_maf_line3_pro.get()))))
                if not float(e_feat_maf_line4_pro.get()) == 0:
                    e_feat_maf_line4_erg.delete  (0, "end")
                    e_feat_maf_line4_erg.insert (0, b_feat_maf_k.cget("text") % (float(e_feat_maf_kurs.get()) / 100 * (100 + float(e_feat_maf_line4_pro.get()))))
                if not float(e_feat_maf_line5_pro.get()) == 0:
                    e_feat_maf_line5_erg.delete  (0, "end")
                    e_feat_maf_line5_erg.insert (0, b_feat_maf_k.cget("text") % (float(e_feat_maf_kurs.get()) / 100 * (100 + float(e_feat_maf_line5_pro.get()))))
                if not float(e_feat_maf_line6_pro.get()) == 0:
                    e_feat_maf_line6_erg.delete  (0, "end")
                    e_feat_maf_line6_erg.insert (0, b_feat_maf_k.cget("text") % (float(e_feat_maf_kurs.get()) / 100 * (100 + float(e_feat_maf_line6_pro.get()))))
                if not float(e_feat_maf_line7_pro.get()) == 0:
                    e_feat_maf_line7_erg.delete  (0, "end")
                    e_feat_maf_line7_erg.insert (0, b_feat_maf_k.cget("text") % (float(e_feat_maf_kurs.get()) / 100 * (100 + float(e_feat_maf_line7_pro.get()))))
            b_feat_maf_lines_cal = tk.Button(f, text="Cal", font=('Courier New', 14, 'bold'), command=feat_maf_lines_cal)
            b_feat_maf_lines_cal.place (x=coord_x + 345, y=coord_y - 25, width=45, height=20)

# Zeit Sync
if 1==1:
    def timek():
        pc_zeit = int("%.0f" % (time.time() * 1000))

        try:
            url = "https://api.binance.com/api/v1/time"
            r = requests.get (url, timeout=4)
            serverzeit = r.json() ["serverTime"]

            diff = int(serverzeit) - int(pc_zeit)
            b_timek.configure (text=diff)
        except Exception as e:
            try:
                t_log_all.insert ("1.0", r.text + "\n\n")
                t_log_all.insert ("1.0", "TIMECORRECTION EXCEPTION\n" + str(e))
            except:
                t_log_all.insert ("1.0", "TIMECORRECTION EXCEPTION CRITICAL\n" + str(e))
    b_timek = tk.Button (f, text=0, font=('Courier New', 10, 'bold'), command=timek)
    b_timek.place (x=540, y=575, width=60, height=20)

# Zeitangabe
if 1==1:

    class zeitangabe(Thread):
        def run(self):
            global ende, zeit
            ende = 1
            while ende == 1:
                try:
                    l_zeitangabe.configure(text=time.strftime("%d.%m.%y %H:%M:%S"))
                    time.sleep(1)
                except:
                    pass


    l_zeitangabe = tk.Label(f, text="00000.00", font=('Courier New', 14, 'bold'),relief="ridge", anchor="w")
    l_zeitangabe.place (x=460, y=530, width=200, height=25)

# Log Textfeld
if 1==1:

    def clear():

        t_log_all.delete ("1.0", "end")

    t_log_all = tk.Text (f,  font=('Courier New', 12, 'bold'), bg="#d0d0d0", relief="sunken")
    t_log_all.place(x=15, y=40, width=665, height=300)
    
    b_log_destroy = tk.Button (f, font=('Courier New', 10, 'bold'), text="Cl", command=clear)
    b_log_destroy.place (x=20, y=15, width=25, height=20)

# Zeitangabe
zeitangabe().start()

f.mainloop()
ende=0
